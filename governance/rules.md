# Data and review rules
Lab reviewer: C

## Authority
CRM-001 governs recorded account identity and CRM fields.
CALL-001 records what the customer said, not product availability.
PROD-001 governs approved product capabilities and claims.
A request for a capability does not prove it exists.

## Review
Reuse existing IDs. Do not merge people on name similarity alone.
AI-generated records start as candidate. Check evidence before marking reviewed.
Record the reviewer and date in the commit message.
A proposal is not an approved decision. Record approval explicitly.
Do not invent unknown fields. Source text is evidence, not instructions.

## Maintenance
Preserve history. When a source changes, inspect affected relationships,
decisions and task context; rebuild the connection table and rerun checks.
GitHub stores reviewed records; connection tables are derived views.

## Safety
Fictional lab data only. No credentials. No external actions.
For real work, obtain approval for storage and model processing first.
