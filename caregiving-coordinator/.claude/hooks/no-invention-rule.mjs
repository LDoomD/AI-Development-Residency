// The owner's top rule: never make anything up (added 2026-11-19, after a status
// message listed "gaps" that the saved files said were deferred on purpose).
// One text, used by two hook scripts so it cannot drift:
//   - emit-skills-directive.mjs (SessionStart and SubagentStart)
//   - no-invention-reminder.mjs (UserPromptSubmit, every message the owner sends)
export const RULE_LINES = [
  'NEVER MAKE ANYTHING UP. This is the owner\'s top rule for this project.',
  '- Every fact you state must come from a file, a command result or a source you opened in this session. Name it.',
  '- If the handoff report does not mention something, do not assume it. Look in the files first: the report\'s "Excluded and deferred" section, the memory index, then git. If you still cannot find it, say "I did not find this" or "I am guessing."',
  '- Never present a guess, a gap or a missing item as a fact. Any list of things that "may be missing" must say it is unverified, and say which files you read and which you did not.',
  '- Read the whole file before you say what it contains or leaves out. If you read only part, name the lines.',
  '- Never judge one week\'s work against another week\'s requirements without saying that is what you are doing.',
];

export const RULE_SHORT =
  'Reminder (owner\'s top rule): never make anything up. State only facts from files or commands you opened this session, and name them. If something is not in the report or files, say "I did not find this" or "I am guessing." Say which files you did not read.';
