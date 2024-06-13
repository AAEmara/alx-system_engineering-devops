Command line for the win Project README

Uploading the images using sftp:

1- Use your local machine with the sftp command as follows:

    $ sftp <username>@<remote hostname>

2- Enter the password after being prompted by your local cmd.

3- Change your current remote working directory using `cd` command:

    sftp> cd <desired remote working directory>

4- Check that you are in the desired remote working directory:

    sftp> pwd
    Remote working directory: /<path to the current remote working directory>

5- Check the current local working directory using `lpwd` command:

    sftp> lpwd
    Local working directory: /<path to the current local working directory>

6- Change your current local working directory using `lcd` command:

    sftp> lcd <desired local working directory>

7- Upload the files you would like to the remote machine using `put` command:

    sftp> put *_9_*

8- Check the remote destination has the required files using `ls` command:

    sftp> ls
