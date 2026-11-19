#!/usr/bin/env node
// UserPromptSubmit hook: adds the owner's "never make anything up" reminder to
// context on every message. Plain stdout from this event is added as context.
import { RULE_SHORT } from './no-invention-rule.mjs';

console.log(RULE_SHORT);
