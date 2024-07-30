# mobaxtermsessionconvert
Convert a MobaXterm Sessions.mxtsessions file to an OpenSSH config file.

MobaXterm offers an option to "Export Sessions" which will result in a proprietary file format which has been reversed by various online resources. I just needed something quick to be able to sync up my sessions with Linux/MacOS clients' SSH config. As such the script only converts the name, host/ip, user, port and keyname.

Meaning it converts a MobaXterm Sessions.mxtsessions file with lines like this:
```
devserver=#109#0%10.0.4.120%22%% %-1%-1% %%22%%0%-1%Interactive shell%Y:\keys\dev.ppk
```
To an OpenSSH config file format such as:
```
Host devserver
    HostName 10.0.4.120
    User dev
    Port 22
    IdentityFile ~/.ssh/dev.openssh.pub
```
Note: You will have to convert your own keys to openssh format and do a search/replace
