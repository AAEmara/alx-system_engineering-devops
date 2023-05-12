Project 0x01. Shell, permissions README

Scripts Description per file:

Task0 0-iam_betty:
Changes to user called "betty" with `su` command.

Task1 1-who_am_i:
Prints the effective username of the current user
using `whoami` command (used in script)
or `id -un` (same effect).

Task2 2-groups:
Prints the names of the groups the current user
is part of using `id` command combined with `-G`
for all group IDs and `-n` option for printing the
names of the groups instead of the IDs.

Task3 3-new_owner:
Changes the owner of the file named "hello" to
the user named "betty" by using the `chown`
command.

Task4 4-empty:
Creates a new empty file called "hello" by using
`touch` command.

Task5 5-execute:
Adds execution permission to the owner of the
file named "hello"; by using the `chmod` command
combined with `u+x` mode parameter.

Task6 6-multiple_permissions:
Adds execution permission to the owner and the
group owner, and read permission to other users;
by using `chmod` command with `ugo`, `+`, and `rx`
file mode bits parameters on the file named
"hello".

Task7 7-everybody:
Adds execution permission to the owner, the 
group owner, and the other users by using `chmod`
command with `ugo`, `+`, and `x` file mode bits
parameters on the file named "hello".
