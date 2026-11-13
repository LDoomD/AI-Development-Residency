# Morgan's Test Case Scenarios
- Source copy: https://app.notion.com/p/0fa9219a4691829aa4678140bda98839
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:13.086Z
- Not saved: none

---

# Background

As part of the working sessions, we're practicing performing QA on a real piece of software. The Tech Fleet Platform is a place where TF members can do what they need for our programs all in one place. We are going to focus on Applications for our testing.

# Features in Scope

1. Members
   1. CRUD general applications
      1. Create a new general application
      2. Read an existing general application
      3. Edit an existing  general application
      4. Delete an existing general application
   2. CRUD project applications
      1. Create a new general application
      2. Read an existing general application
      3. Edit an existing  general application
      4. Delete an existing general application
2. Project coordinator flows (Admins)
   1. Recruiting center - reviewing applications that have been submitted
   2. Setting the status of applications

# Use Cases

1. Create a new general application
   1. Use Case 1: An existing member user submitting a new general application
   2. Use Case 2: An existing member saving a draft of a new general application after starting it for the first time
2. Read an existing general application
   1. Use Case 3: Viewing a previously submitted general application
   2. Use Case 4: Viewing a draft general application
3. Edit an existing  general application
   1. Use Case 5: Edit a previously submitted general application
   2. Use Case 6: Editing a draft general application
4. Delete an existing general application
   1. Use Case 7: Deleting a previously submitted general application as a member user
   2. Use Case 8: Deleting a previously submitted general application as a admin user
   3. Use Case 9: Deleting a draft general application as a member user
5. Create a new project phase application
6. Read an existing project phase application
7. Edit an existing  project phase application
8. Delete an existing project phase application
9. Recruiting center - reviewing applications that have been submitted
   1. Use Case 10: Admin review the number of people who applied to other projects on the Application Analysis page
   2. Use Case 11: Admin determines if the project is ready to recruit
   3. Use Case 12: Admin reviews application submissions on the Project Roster
10. Setting the status of applications
    1. Use Case 13: Admin changes the status of a single application for a single person
    2. Use Case 14: Admin invites a person to a project training team
11. Sending project blast emails to people who apply
    1. Use Case 15: Admin sending an email to people who applied

# BDD Scenarios

**Use Case 1: An existing member user submitting a new general application**

### BDD 1: Viewing General Applications Page That Is Empty ("Happy Path")

```feature
GIVEN I am an existing member of techfleet.network
AND my account is not locked
AND I am logged into the system
AND I have never created a general application before
WHEN I navigate to applications 
AND I click on the general applications card
THEN I should be taken to the general application 
AND I should be navigated to the intro section
```

### BDD 2: Submitting the General Application for the First Time (Happy Path)

```feature
GIVEN I am an existing member of techfleet.network
AND my account is not locked
AND I am logged into the system
AND I have never created a general application before
AND I have navigated to the General Applications page
AND I click on the general applications card
WHEN I am on the general application page
AND I fill out all of the sections on the general application
AND I navigate to the Review page
THEN the submit application button should be clickable 
AND I can edit any section by clicking on the pencil
AND I can see whatever section is complete
AND I can see the actual fields that were filled out in all sections 
```

```feature
GIVEN I am currently on the general application 
AND I have completed all sections
AND I have filled out all of the fields correctly
WHEN I navigate to the Review page
AND I click on Submit Application
THEN The entire general application should be saved forever to my account
AND I should be able to get back to the general application at any time to edit it
AND I should receive system feedback when the system saves the application
```

### BDD 3: User did not finish their profile before trying to submit the application ("Non-Happy Path")

```feature

```

### BDD 3: User left the general app completely blank and tries to submit ("Edge Case")

### BDD 3: User tries to perform SQL Injection into a general application field ("Edge Case")

## Use Case 5: Edit a previously submitted general application

## Use Case 6: Editing a draft general application 

## Use Case 7: Deleting a previously submitted general application as a member user

**Use Case 10: Admin review the number of people who applied to other projects on the Application Analysis page**

## BDD Scenario: Showing the Total Readiness Score

```feature
GIVEN I am an admin 
AND I have an existing acccount 
AND I am logged into the system
AND there is an existing project that is under "Recruiting" status
AND there are at least one submitted project application under the project
WHEN I click on the project card from Recruiting Center page
THEN on page load, I see the status whether the project is ready for recruiting or not
AND the status is based on the proper calculations in the system for determining project recruiting readiness
AND the status is yellow if it's "Almost Ready" 
AND the status is green if it's "Ready"
```

```feature
GIVEN I am an admin 
AND I have an existing acccount 
AND I am logged into the system
AND there is an existing project that is under "Recruiting" status
AND there are at least one submitted project application under the project
WHEN I click on the project card from Recruiting Center page
THEN on page load, I see the button to show the readiness calculation
AND it uses the same design system component that's already in the system
AND it's labeled "Score details"
```

```feature
GIVEN I am an admin 
AND I have an existing acccount 
AND I am logged into the system
AND there is an existing project that is under "Recruiting" status
AND there are at least one submitted project application under the project
AND I have navigated to a project under Recruiting Center
WHEN I click on Score Details
THEN A popup opens
AND the popup is designed with the same design component as what's already in the system
AND the popup shows the accurate information about the score calculation
AND I can close it by clicking on the X at the top right corner
```

## BDD Scenario: Showing the Calculation of the Readiness Score

# Test Case Scenarios

**Use Case 1: An existing member user submitting a new general application**

**Test Case Scenario 1: Creating a New General Application**

#### Preconditions

1. An existing USER account (not admin) 
2. The account has NEVER completed a general application
3. Discord account on the user's profile is NOT completed

#### Steps to Complete

1. Login with USER
2. Navigate to Applications
3. Click on General Application
4. Complete the Intro section
   1. "Tech Fleet project trainees are expected to commit 15 to 20 hours on project team training. This is flexible, and your team builds the schedule together based on their availability. Are you committed to contribute 15 to 20 hours a week during project training? \*" Enter yes 
   2. Portfolio URL leave blank
   3. LinkedIn URL leave blank 
   4. Click Next
5. Complete all fields on the profile
   1. First and last name
   2. Connect to Discord
   3. Enter time zone
   4. enter location
   5. Enter experience 
   6. Enter education
   7. Enter professional goals 
   8. Enter notifications 
6. Complete Engagement section
7. Complete Agile section
8. Complete Service Leadership section
9. Go to Review section

#### Expected Results

1. The system will tell you if you have missed any fields at the top 
2. The system will show the state of each section's completedness
3. The system allows the user to hit the edit button on each section to edit, and that should successfully navigate you back to that section
4. If there are any sections missing, the system will prevent you from submitting the form
5. Once submitted, the record is permanently saved to the user's account
6.  The user can go back to the same general app through the same page and edit the general app (another test case) 
7. The system should show a toast notification once the record is successfully saved
8. If there was an error submitting, then the system should be showing a toast error notification

#### Actual Results

| Step | Input | Expected Result | Actual | Pass or Fail? | Notes |
| --- | --- | --- | --- | --- | --- |
| Login | morgandenner1@gmail / PW | Success | Successfully logged in, it took me to the welcome page, and the dashboard, and had me fill out my profile | Pass |  |
| Navigate to Applications | Click | Page load | Page loaded | Pass |  |
| Open General Applications | Click | Page load, and send the user to the first section | Page loaded, and it did properly take my to the section  | Pass |  |
| Complete the intro section | "Yes" / leave blank / leave blank |   • I am navigated to the next section<br />  • My application is saved as a draft in under 3 seconds |   • I was taken to the next section<br />  • NOT GOOD: My application was saved as a draft in 30 seconds | Failure | The draft save took way longer than expected. It did save as a draft. I checked what happened on reload, and it did properly save my data. It just took over 30 seconds. This may be a performance issue with some layer like domain, data source, presentation. Needs investigation.  |
|  |  |  |  |  |  |

**Use Case 10: Admin review the number of people who applied to other projects on the Application Analysis page**

**Test Case: View of the Recruiting Center**

## Pre-Conditions

1. A user account must be set up in the TF platform and active
2. The account must have admin privileges 
3. The account must not be inactive or locked
4. There is one client existing in the system
5. There is one project associated with that client
6. The status of the project is "Recruiting" 
7. There is at least 5 application submitted to the project that is being tested.

## Steps to Complete

1. Login as admin
2. Navigate to the Recruiting Center
3. Find the project that has at least 5 applications under "Recruiting" status
4. Click on the project

## Expected Results

1. The page loads according to the prototypes that were made
2. You can see the Recruiting Status on the top of the page, either Almost Ready or Ready
3. You can click on the Score details and see a popup of rules
4. You can see how many people applied to all of the different roles 
5. You can see, for each role, how many people ONLY applied to this project
6. You can see, for each role, how many people applied to OTHER projects

# Actual Results

| Step | Input | Expected Result | Actual | Pass or Fail? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Test Case: Taking Action on the Recruiting Center**

## Pre-Conditions

1. A user account must be set up in the TF platform and active
2. The account must have admin privileges 
3. The account must not be inactive or locked
4. There is one client existing in the system
5. There is one project associated with that client
6. The status of the project is "Recruiting" 
7. There is at least 5 application submitted to the project that is being tested.

## Steps to Complete

1. Login as admin
2. Navigate to the Recruiting Center
3. Find the project that has at least 5 applications under "Recruiting" status
4. Click on the project

## Expected Results

1. I can click on "**6** applied to other projects too" for each role to see the breakdown of what projects people have applied to for that specific role
2. Every role has this ability
3. Additional Roles section has this ability as well 

# Actual Results

| Step | Input | Expected Result | Actual | Pass or Fail? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
