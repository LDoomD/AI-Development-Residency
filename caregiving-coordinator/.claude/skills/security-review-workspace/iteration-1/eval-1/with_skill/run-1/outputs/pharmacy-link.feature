# features/backend-input/pharmacy-link.feature
#
# This is the "shared feature-file index" entry the owasp-secure-coding-bdd
# skill requires for every control applied to routes/pharmacy-link.js. This
# project (caregiving-coordinator) has no bdd-comprehensive-testing skill, no
# features/ directory, and no CI runner installed yet, so this file cannot
# actually be indexed or executed today. It is written as the file that
# SHOULD be committed at features/backend-input/pharmacy-link.feature the
# moment that scaffolding exists, so the controls below are not shipped as
# untested prose in the meantime. See security-decision-record.md for exactly
# what is still missing and the waiver that covers the gap until it's built.

@owasp:sql-injection @owasp:query-parameterization
Feature: Pharmacy portal linking is free of SQL injection
  As the caregiving-coordinator team
  We want pharmacy-link queries to bind user input instead of concatenating it
  So that an attacker cannot change query structure through any field this route accepts

  @security @owasp:sql-injection @usecase:pharmacy-link-create-injection @audience:backend @behavior-class:negative @severity:critical
  Scenario: Creating a pharmacy link rejects a SQL injection payload in careRecipientId
    Given an authenticated caregiver with a care relationship to care recipient "42"
    When the caregiver POSTs to /pharmacy-link with careRecipientId "42'; DROP TABLE pharmacy_links; --"
    Then the request is rejected or stored as a literal value with no SQL structure change
    And the pharmacy_links and care_relationships tables still exist and are unmodified
    And the insert runs as a parameterized statement so the input is bound as data, not SQL

  @security @owasp:sql-injection @usecase:pharmacy-link-read-injection @audience:backend @behavior-class:negative @severity:critical
  Scenario: Reading a pharmacy link rejects a SQL injection payload in the URL id
    Given an authenticated caregiver
    When the caregiver GETs /pharmacy-link/1' OR '1'='1
    Then no pharmacy link rows are returned for any care recipient other than "1"
    And the lookup runs as a parameterized statement so the input is bound as data, not SQL

@owasp:idor @owasp:authorization
Feature: Pharmacy portal credentials are scoped to the caregiver's own care recipients
  As a family using caregiving-coordinator
  We want pharmacy credentials visible only to caregivers with an actual relationship to that care recipient
  So that one family's linked account cannot be read or created by an unrelated user

  @security @owasp:idor @owasp:authorization @usecase:pharmacy-link-horizontal-escalation @audience:backend @behavior-class:negative @severity:critical
  Scenario: A caregiver cannot read another family's pharmacy link by changing the id
    Given Caregiver A has a pharmacy link for care recipient "42"
    And Caregiver B has no care relationship with care recipient "42"
    When Caregiver B GETs /pharmacy-link/42
    Then the response is 404
    And the lookup is scoped to care recipients the authenticated caregiver has a relationship with

  @security @owasp:authorization @usecase:pharmacy-link-create-without-relationship @audience:backend @behavior-class:negative @severity:critical
  Scenario: A caregiver cannot create a pharmacy link for a care recipient they are not related to
    Given an authenticated caregiver with no care relationship to care recipient "99"
    When the caregiver POSTs to /pharmacy-link with careRecipientId "99"
    Then the response is 403
    And no row is inserted into pharmacy_links

  @security @owasp:authorization @usecase:pharmacy-link-trusts-session-not-body @audience:backend @behavior-class:negative @severity:high
  Scenario: Creating a pharmacy link uses the authenticated session, not a client-supplied user id
    Given Caregiver A is authenticated
    When Caregiver A POSTs to /pharmacy-link with body field userId set to Caregiver B's id
    Then the stored pharmacy_links row records Caregiver A as the owning user
    And the client-supplied userId field in the request body is ignored

@owasp:crypto-storage
Feature: Pharmacy portal passwords are encrypted at rest, not stored or logged in plain text
  As the caregiving-coordinator team
  We want linked pharmacy portal passwords unreadable from a stolen database copy
  So that a breach of pharmacy_links does not hand out live pharmacy-portal credentials

  @security @owasp:crypto-storage @usecase:pharmacy-password-at-rest-confidentiality @audience:backend @behavior-class:positive @severity:critical
  Scenario: A linked pharmacy password is stored as authenticated ciphertext, never plain text
    Given a caregiver links a pharmacy portal account with a password
    When the password is persisted to pharmacy_links
    Then the stored value is AES-256-GCM ciphertext with a unique IV, not the plain text password
    And the decryption key is not present in the pharmacy_links table or row

  @security @owasp:crypto-storage @usecase:pharmacy-password-never-returned @audience:backend @behavior-class:negative @severity:high
  Scenario: The pharmacy password is never returned in an API response
    Given a caregiver has a linked pharmacy account
    When any authorized caregiver GETs /pharmacy-link/:careRecipientId
    Then the response contains the username but never the password or its ciphertext

@owasp:logging
Feature: Pharmacy portal linking never logs credentials
  As the caregiving-coordinator team
  We want pharmacy-link log entries free of secrets
  So that application logs cannot become a second place credentials leak from

  @security @owasp:logging @usecase:pharmacy-link-no-secret-in-logs @audience:backend @behavior-class:negative @severity:high
  Scenario: Creating a pharmacy link logs the event without the username or password
    Given a caregiver links a pharmacy portal account with username "jsmith" and a password
    When the pharmacy_link_created event is logged
    Then the log entry contains the acting user id, the care recipient id, and a timestamp
    And the log entry does not contain the pharmacy username or the pharmacy password in any form
