import os
os.chdir('/Users/oooo/Documents/py/py_path/2022/basic/basic')

# print(dir(os))
# access(path,mode)
# os.F_OK  — Found
# os.R_OK  — Readable
# os.W_OK  — Writable
# os.X_OK  — Executable
# os.chdir('/Users/oooo/Desktop')
# print(os.access('Screenshot 2024-11-05 at 4.28.05 PM.png',os.R_OK))

#### chdir(path)changes the current working directory 


##### chflags(path,flags)
# chflags() sets path flags to the numeric flags. These flags may take a combination(bitwise OR) of the following values:
# most flag # Need SuperUser Privileges. Also, some flags don’t work on all systems.
# os.UF_NODUMP – Don’t dump the file
# os.UF_IMMUTABLE − You may not change the file
# os.UF_APPEND − You may only append to the file
# os.UF_NOUNLINK – You may not rename or delete the file
# os.UF_OPAQUE − The directory is opaque when we view it through a union stack
# os.SF_ARCHIVED – You may archive the file
# os.SF_IMMUTABLE – You may not change the file
# os.SF_APPEND – You may only append to the file
# os.SF_NOUNLINK – You may not rename or delete the file
# os.SF_SNAPSHOT − It is a snapshot file


### chmod(path,mode)
# The mode may be on of the following values(or a bitwise OR combination of them):
# stat.S_ISUID − Set user ID on execution
# stat.S_ISGID − Set group ID on execution
# stat.S_ENFMT – Enforced record locking
# stat.S_ISVTX – After execution, save text image
# stat.S_IREAD − Read by owner
# stat.S_IWRITE − Write by owner
# stat.S_IEXEC − Execute by owner
# stat.S_IRWXU − Read, write, and execute by owner
# stat.S_IRUSR − Read by owner
# stat.S_IWUSR − Write by owner
# stat.S_IXUSR − Execute by owner
# stat.S_IRWXG − Read, write, and execute by group
# stat.S_IRGRP − Read by group
# stat.S_IWGRP − Write by group
# stat.S_IXGRP − Execute by group
# stat.S_IRWXO − Read, write, and execute by others
# stat.S_IROTH − Read by others
# stat.S_IWOTH − Write by others
# stat.S_IXOTH − Execute by others



# chroot(path)
# chroot Python os Module alters the current process’ root directory to the given path.
# Need SuperUser Privileges
# >>> os.chroot("/Photos")



# Close(fd) and Closerange(fd_low,fd_high)
# This Python os module closes the associated file with descriptor fd.
# fd=os.open('Test.txt',os.O_RDWR)
# >>> os.close(fd)

# os.chdir('/Users/oooo/Desktop')
# print(os.access('Test.txt',os.R_OK))


# fd0 = os.open( "Today.txt", os.O_RDWR) #, os.O_RDWR | os.O_CREAT
# Open multiple file descriptors
# fd1 = os.open("file1.txt", os.O_RDWR | os.O_CREAT)
# fd2 = os.open("file2.txt", os.O_RDWR | os.O_CREAT)
# fd3 = os.open("file3.txt", os.O_RDWR | os.O_CREAT)
# os.write(fd0, "Testing".encode()) # .encode() or b'Testing' 
# Close all file descriptors in the range [fd1, fd3+1)
# os.closerange(fd0, fd3 + 1)

# # Open several files
# fds = [os.open(f"file{i}.txt", os.O_RDWR | os.O_CREAT) for i in range(5)]
# # Write to all of them
# for i, fd in enumerate(fds):
#     os.write(fd, f"Data for file {i}\n".encode())
# # Close all file descriptors in a range
# os.closerange(fds[0], fds[-1] + 1)



# dup(fd) duplicate of the file descriptor fd. || dup2(fd,fd2) dup2() duplicates the descriptor fd to fd2. And if necessary, it closes fd2 first.
# Duplicates a file descriptor. It creates a new file descriptor that points to the same file or resource as the original descriptor.
# Does not modify the file or resource; it just creates another reference (descriptor) to the same open file or resource.
# fd = os.open( "Today.txt", os.O_RDWR)
# d_fd = os.dup( fd )
# os.write(d_fd, b"Testingdub")
# os.closerange( fd, 1000)

# Open a file
# fd1 = os.open("Today.txt", os.O_RDWR | os.O_CREAT)
# # Duplicate the file descriptor
# fd2 = os.dup(fd1)
# # Write data using the original descriptor
# os.write(fd1, b"Original descriptor writes this line.\n")
# # Write data using the duplicate descriptor
# os.write(fd2, b"Duplicate descriptor writes this line.\n")
# data = os.read(fd2, 1024)
# print(data)
# # Close both descriptors
# os.close(fd1)
# os.close(fd2)

# ### Python os Module dup(fd) returns a duplicate of the file descriptor fd.
# # Open multiple files for reading and writing
# fd_in = os.open("Today.txt", os.O_RDONLY)  # For reading
# fd_out = os.open("output.txt", os.O_RDWR | os.O_CREAT)  # For writing
# # Read from input and write to output
# data = os.read(fd_in, 1024)  # Read up to 1KB
# os.write(fd_out, data)       # Write the data to the output file
# # Close both file descriptors
# os.close(fd_in)
# os.close(fd_out)

# # 3. Inter-Process Communication (IPC)
# # When using pipes or sockets, multiple descriptors are created to represent each end of the pipe or socket connection. These are used to send and receive data between processes.
# # Example: Using os.pipe() for IPC

# # Create a pipe with two file descriptors
# r_fd, w_fd = os.pipe()  # r_fd: read end, w_fd: write end
# # Write to the write-end of the pipe
# os.write(w_fd, b"Message through the pipe!")
# # # Read from the read-end of the pipe
# data = os.read(r_fd, 1024)
# print(f"Received: {data.decode()}")  # Output: Received: Message through the pipe!
# # # Close both ends of the pipe
# os.close(r_fd)
# os.close(w_fd)

# # 4. Concurrent Loggers or Streams
# # In applications that generate multiple logs (e.g., error logs, access logs, or debug logs), separate descriptors may be used for each log file to handle simultaneous writes.
# # Open multiple log files
# fd_error = os.open("error.log", os.O_RDWR | os.O_CREAT)
# fd_access = os.open("access.log", os.O_RDWR | os.O_CREAT)
# # Write errors to the error log
# os.write(fd_error, b"ERROR: Something went wrong.\n")
# # Write access logs to the access log file
# os.write(fd_access, b"ACCESS: User visited homepage.\n")
# # Close log file descriptors
# os.close(fd_error)
# os.close(fd_access)

# # 5. When working with Subprocess
# # When spawning subprocesses, the parent process may pass file descriptors to the child process for communication or redirection.
# import subprocess
# # Open a log file for the subprocess output
# fd_log = os.open("subprocess.log", os.O_RDWR | os.O_CREAT)
# # Spawn a subprocess and redirect its output
# subprocess.run(["echo", "Hello from subprocess"], stdout=fd_log)
# # Close the log file descriptor
# os.close(fd_log)

# #6. Network Programming
# # When dealing with network sockets, each connection gets a unique descriptor. A server typically maintains multiple descriptors for each connected client.
# import socket
# # Create a listening socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 12345))
# server_socket.listen(5)
# print("Server is listening...")
# while True:
#     # Accept a new client
#     client_socket, addr = server_socket.accept()
#     print(f"New connection from {addr}")
#     # Get the file descriptor of the client socket
#     fd_client = client_socket.fileno()
#     # Write a message to the client using its descriptor
#     os.write(fd_client, b"Welcome to the server!\n")
#     # Close the client descriptor
#     client_socket.close()
    
# #7- Low-Level Resource Management
# # In some applications (e.g., file systems, database systems, or embedded systems), multiple file descriptors are used to manage different resources (e.g., files, devices, or sockets) efficiently.
# import fcntl
# # # Open a file for locking
# fd1 = os.open("resource1.txt", os.O_RDWR | os.O_CREAT)
# fd2 = os.open("resource2.txt", os.O_RDWR | os.O_CREAT)
# # Lock each file descriptor
# fcntl.flock(fd1, fcntl.LOCK_EX)
# fcntl.flock(fd2, fcntl.LOCK_EX)
# print("!!!!!!!Both resources locked.")
# # Release locks and close descriptors
# fcntl.flock(fd1, fcntl.LOCK_UN)
# fcntl.flock(fd2, fcntl.LOCK_UN)
# print("!!!!!!!Both resources Released.")
# os.close(fd1)
# os.close(fd2)

# # otherUses
# # 1 Logging and Auditing
# # 2 Debugging and dignostic
# # 3 Memory Efficiency: Avoid memory overflow by offloading data to disk.
# # 4 Batch Processing and Offline Analysis - Why: I/O stored in files can be processed later in bulk or analyzed offline.
# # 5 Backup and Recovery


# fd = os.open( "/Users/oooo/Documents/py/py_path/2022/basic/basic/testdir_for_0_os_module", os.O_RDONLY )
# print("Current working dir : %s" % os.getcwd())
# os.fchdir(fd)
# print("Current working dir : %s" % os.getcwd())
# os.close( fd )



# # fchmod(fd,mode)
# This Python os Module alters the file mode of the file, specified by fd, to the numeric mode.
# The mode may be one of the following (or an ORed combination of):
# stat.S_ISUID − Set user ID on execution
# stat.S_ISGID − Set group ID on execution
# stat.S_ENFMT − Record locking enforced
# stat.S_ISVTX − Save text image after execution
# stat.S_IREAD − Read by owner
# stat.S_IWRITE − Write by owner
# stat.S_IEXEC − Execute by owner
# stat.S_IRWXU − Read, write, and execute by owner
# stat.S_IRUSR − Read by owner
# stat.S_IWUSR − Write by owner
# stat.S_IXUSR − Execute by owner
# stat.S_IRWXG − Read, write, and execute by group
# stat.S_IRGRP − Read by group
# stat.S_IWGRP − Write by group
# stat.S_IXGRP − Execute by group
# stat.S_IRWXO − Read, write, and execute by others
# stat.S_IROTH − Read by others
# stat.S_IWOTH − Write by others
# stat.S_IXOTH − Execute by others
# or
# Permission Mode Reference
# Octal Value	Permission	Description
# 0o400	Read by owner	The owner of the file can read it.
# 0o200	Write by owner	The owner of the file can write to it.
# 0o100	Execute by owner	The owner of the file can execute it.
# 0o040	Read by group	Members of the group can read it.
# 0o020	Write by group	Members of the group can write to it.
# 0o010	Execute by group	Members of the group can execute it.
# 0o004	Read by others	Other users can read it.
# 0o002	Write by others	Other users can write to it.
# 0o001	Execute by others	Other users can execute it.

# import stat
# fd = os.open( "/Users/oooo/Documents/py/py_path/2022/basic/basic/testdir_for_0_os_module", os.O_RDONLY )
# # Get initial file mode
# initial_mode = os.fstat(fd).st_mode
# os.fchmod( fd, stat.S_IXGRP)
# os.fchmod(fd, stat.S_IWOTH)
# os.fchmod(fd, stat.S_IREAD) # Ready by owner if we skip this i will not be able to modifi permission in below code 
# # because to change permission i will have to open file first in a mode i have the access to
# print("Changed mode successfully!!")
# os.close(fd)
# ##############
# fd = os.open( "/Users/oooo/Documents/py/py_path/2022/basic/basic/testdir_for_0_os_module", os.O_RDONLY )
# # Get initial file mode
# initial_mode = os.fstat(fd).st_mode
# os.fchmod( fd, stat.S_IEXEC)
# os.fchmod(fd, stat.S_IRWXU)
# print("Changed again successfully!!")
# os.close(fd)




#  fchown(fd,uid,gid)
# fchown() alters the owner and the group id of the file specified by fd to the numeric uid and gid.
# Setting an id to -1 leaves it unchanged.
# Here are some real-world scenarios where fchown() might be used:
# 1. System Administration:
# File System Management: When creating or modifying file systems, administrators often need to set appropriate ownership and permissions for files and directories. This ensures proper access control and security.
# Log File Rotation: To automate log file rotation, scripts can use fchown() to transfer ownership of old log files to a specific user or group for archiving or analysis.
# User Management: When creating new user accounts, administrators might use fchown() to assign ownership of home directories and other files to the newly created user.
# 2. Security:
# File Permissions: By changing ownership and permissions, administrators can control who can access and modify files. This is essential for protecting sensitive data.
# Security Audits: fchown() can be used to track file ownership changes and identify potential security breaches.
# 3. Scripting and Automation:
# Backup Scripts: Scripts that automate backups can use fchown() to set appropriate ownership and permissions on backup files.
# Deployment Scripts: Deployment scripts might use fchown() to adjust ownership and permissions of deployed files and directories to ensure correct functionality and security.
# 4. Software Installation:
# Package Managers: Package managers like RPM and DEB use fchown() to set appropriate ownership and permissions for installed files.
# 5. Web Server Configuration:
# Web Server Logs: Web server administrators can use fchown() to set ownership and permissions for log files to ensure proper rotation and analysis.
# Remember:
# Root Privileges: Using fchown() often requires root privileges, as it involves changing ownership of files and directories.
# Caution: Misusing fchown() can have security implications. Always exercise caution when changing ownership and permissions.
# Best Practices: Follow security best practices and avoid unnecessary changes to file ownership and permissions.
# fd = os.open( "/Users/oooo/Documents/py/py_path/2022/basic/basic/testdir_for_0_os_module", os.O_RDONLY )
# os.fchown( fd, 100, -1)
# os.fchown( fd, -1, 50)
# print("Changed ownership successfully!!")
# os.close( fd )


# fdatasync() forces writing the file with filedescriptor fd to disk. This, however, doesn’t force update on metadata.
fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, b"Testing")
os.fdatasync(fd)
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print(f"Read String is {str}")
os.close(fd)