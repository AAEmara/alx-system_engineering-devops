# 0x19. Postmortem
## Issue Summary
From 02:47 AM UTC to 05:00 AM UTC, our Wordpress Website was returning a 500
error response messages. The issue impacted 100% o the users using the Website
at the time. The root cause was an invalid library file name.
## Timeline (all times Greenwitch, United Kingdom)
- 02:47 Configurations has been modified.
- 02:58 Customer Reported that the Website is down, due to a server error.
- 03:03 The issue was assigned to the Fullstack engineer.
- 03:05 Checked that the server was listenting on the right port, and the 
running processes.
= 03:08 The running server was listening on the right port.
- 03:15 Checked the running processes and traced the suspected process that
is causing the error using `strace`. 
- 04:15 Detected the invalid library file name and changed its name to the
correct name manually.
- 04:15 The service was 100% back.
- 04:34 The solution was automated using `puppet`.
- 05:00 The puppet manifest was tested and pushed.
## Root Cause and Resolution
The issue occured when a user tried to access our Website and got a 
`500 Internal Server Error`, which was reported to the customer service
and then assigned to the Fullstack Engineer on the call.
The Fullstack Engineer found that the server was listening on the right
port with no problems. After that he investigated the running server
using the `strace` utitlity to understand what was causing the error.
The error was caused by an invalid library file name, which had a typo
in its extension.
This typo was fixed manually and ensured that the service is back online.
Then he automated the solution of this issue using `puppet`.
## Corrective and Preventative Measures
A monitoring service should be used to notify the team with any issues.
