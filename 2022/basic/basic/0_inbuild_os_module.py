import os
os.chdir('/Users/oooo/Documents/py/py_path/2022/basic/basic')

print(dir(os))

#1. access(path,mode)#access to a path
# os.F_OK  — Found
# os.R_OK  — Readable
# os.W_OK  — Writable
# os.X_OK  — Executable
# os.chdir('/Users/oooo/Desktop')
# print(os.access('Screenshot 2024-11-05 at 4.28.05 PM.png',os.R_OK))

#### 2.chdir(path)changes the current working directory 

#####3. chflags(path,flags)
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


###4. chmod(path,mode)
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



# 5 &. chroot(path)
# chroot Python os Module alters the current process’ root directory to the given path.
# Need SuperUser Privileges
# >>> os.chroot("/Photos")



#6 & 7 Close(fd) and Closerange(fd_low,fd_high)
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



# 8 & 9 dup(fd) duplicate of the file descriptor fd. || 
# dup2(fd,fd2) dup2() duplicates the descriptor fd to fd2. And if necessary, it 
# closes fd2 first.
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

# # C. Inter-Process Communication (IPC)
# # When using pipes or sockets, multiple descriptors are created 
# to represent each end of the pipe or socket connection.
#  These are used to send and receive data between processes.
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

# # D. Concurrent Loggers or Streams
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

# # E. When working with Subprocess
# # When spawning subprocesses, the parent process may pass file descriptors to the child process for communication or redirection.
# import subprocess
# # Open a log file for the subprocess output
# fd_log = os.open("subprocess.log", os.O_RDWR | os.O_CREAT)
# # Spawn a subprocess and redirect its output
# subprocess.run(["echo", "Hello from subprocess"], stdout=fd_log)
# # Close the log file descriptor
# os.close(fd_log)

# #F. Network Programming
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
    
# # G- Low-Level Resource Management
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
# # H Logging and Auditing
# # I Debugging and dignostic
# # J Memory Efficiency: Avoid memory overflow by offloading data to disk.
# # K Batch Processing and Offline Analysis - Why: I/O stored in files can be processed later in bulk or analyzed offline.
# # L Backup and Recovery


# fd = os.open( "/Users/oooo/Documents/py/py_path/2022/basic/basic/testdir_for_0_os_module", os.O_RDONLY )
# print("Current working dir : %s" % os.getcwd())# c(Current)(wroking)(dir)


# 10. fchdir(fd)
# fchdir() alters the current working directory to the directory that the file descriptor fd represents.
# os.fchdir(fd)#For this, it is mandatory that the descriptor must refer to an opened directory, and not to an open file
# os.chdir("/var/www/html" )
# print("Current working dir : %s" % os.getcwd())
# fd = os.open( "/tmp", os.O_RDONLY )
# os.fchdir(fd)
# print("Current working dir : %s" % os.getcwd())
# os.close( fd )



# 11 fchmod(fd,mode)
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




# 12 fchown(fd,uid,gid)
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


# 13 fdatasync() forces writing the file with filedescriptor fd to disk. This, however, doesn’t force update on metadata.
# fd = os.open( "Today.txt", os.O_RDWR)
# os.write(fd, b"Testing")
# os.fdatasync(fd)
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print(f"Read String is {str}")
# os.close(fd)

# lseek(fd,pos,how) lseek() doesn’t return any value.
# lseek() will set the current position of the descriptor fd to the specified position pos. ‘how’ modifies it.


# 14. fdopen(fd[, mode[, bufsize]])
# fdopen(), Python os Module returns an open file object. 
# This object is connected to the descriptor fd.
# Once you do this, you can perform all defined functions on the file object.
# Key Differences
# Aspect	| os.open	|   os.fdopen
# Purpose	Opens a file at a low system level.	Converts a file descriptor to a file object.
# Returns	A file descriptor (integer).	A file object.
# Direct Read/Write	Requires os.read/os.write.	Use Python file methods like .read().
# High-Level Support	No built-in support for high-level methods.	Provides high-level file operations.
# Flags	Requires explicit flags (os.O_RDWR).	Requires high-level mode strings ('r+').
# fd = os.open( "Today.txt", os.O_RDWR)
# fo = os.fdopen(fd, "w+")
# print (f"Current I/O pointer position {fo.tell()}")
# fo.write( "Python is a great language.\nYeah its great!!\n");
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print (f"Read String is {str}")
# print (f"Current I/O pointer position {fo.tell()}")
# fo.close()


# 15. fpathconf(fd, name)
# fpathconf() returns system configuration information that is relevant to an open file.

# This is quite similar to the unix system call fpathconf(). It also accepts similar arguments.

# Sample usage:

# fd = os.open( "Today.txt", os.O_RDWR)
# print (f"{os.pathconf_names}")
# no = os.fpathconf(fd, 'PC_LINK_MAX')
# print (f"Maximum number of links to the file: {no}")
# no = os.fpathconf(fd, 'PC_NAME_MAX')
# print (f"Maximum length of a filename :{no}")
# os.close( fd)

# It is a low-level function that allows you to query file-specific limits and options, such as the maximum length of a filename or the maximum number of symbolic links that can be followed.

# Usage
# os.fpathconf(fd, name)
# fd: The file descriptor of the file you want to query. You can get a file descriptor by opening a file using functions like os.open.
# name: The name of the configuration option you want to query. This can be a string or an integer constant from the os module (e.g., 'PC_NAME_MAX', os.pathconf_names['PC_NAME_MAX']).
# What It Does
# The function queries file-specific limits or options, as defined by the POSIX fpathconf system call.
# It is useful for retrieving information that depends on the specific file system where the file resides. For example, the maximum allowable filename length (PC_NAME_MAX) can vary depending on the file system.
# Common Configuration Options
# The following are common name values (constants) that can be used with os.fpathconf:

# Name	Description
# 'PC_LINK_MAX'	Maximum number of links to the file.
# 'PC_MAX_CANON'	Maximum size of a canonical input line.
# 'PC_MAX_INPUT'	Maximum size of an input queue.
# 'PC_NAME_MAX'	Maximum length of a filename in the directory.
# 'PC_PATH_MAX'	Maximum length of a relative pathname when the file is the base.
# 'PC_PIPE_BUF'	Maximum size of a write to a pipe that is guaranteed to be atomic.
# 'PC_CHOWN_RESTRICTED'	Whether the use of chown is restricted to the superuser.
# 'PC_NO_TRUNC'	Whether file names longer than PC_NAME_MAX are truncated.
# 'PC_SYNC_IO'	Whether synchronous I/O is supported.
# 'PC_ASYNC_IO'	Whether asynchronous I/O is supported.
# You can list all available options with os.pathconf_names.

# Example
# Querying the Maximum Filename Length for a File Descriptor
# import os

# # Open a file to get its file descriptor
# fd = os.open("example.txt", os.O_CREAT | os.O_RDWR)

# # Query the maximum filename length for the file's file system
# name_max = os.fpathconf(fd, 'PC_NAME_MAX')
# print(f"Maximum filename length: {name_max}")

# # Close the file descriptor
# os.close(fd)
# List All Configurable Options
# import os

# # Print all available configuration options
# print(os.pathconf_names)


# 16. fstat(fd) & 29 lstate(path)
# Python os Module fstat() returns information about the file pertaining to the fd.
# Let’s take a look at the structure fstat() returns:

# Imagine you’re already holding a book (you’ve already opened it).
# With fstat(), you’re asking for the details about the book you’re holding:
# How many pages it has.
# Who wrote it.
# When it was published.

# lstat() is helpful when you’re dealing with a symlink (bookmark) and need to know about the link itself, not what it points to.

# st_dev − ID of device containing file
# st_ino − inode number
# st_mode – protection
# st_nlink − number of hard links
# st_uid − user ID of owner
# st_gid − group ID of owner
# st_rdev − device ID (if special file)
# st_size − total size, in bytes
# st_blksize − blocksize for filesystem I/O
# st_blocks − number of blocks allocated
# st_atime − time of last access
# st_mtime − time of last modification
# st_ctime − time of last status change

# fd = os.open( "Today.txt", os.O_RDWR)
# info = os.fstat(fd)
# print (f"File Info: {info}")
# print (f"UID of the file: {info.st_uid}")
# print (f"GID of the file: {info.st_gid}")
# os.close(fd)


# 17. fstatvfs(fd)
# This Python os module returns information pertaining to the file system containing the file linked with file descriptor fd.

# This is the structure it returns:

# f_bsize − file system block size
# f_frsize − fragment size
# f_blocks − size of fs in f_frsize units
# f_bfree − free blocks
# f_bavail − free blocks for non-root
# f_files – inodes
# f_ffree − free inodes
# f_favail − free inodes for non-root
# f_fsid − file system ID
# f_flag − mount flags
# f_namemax − maximum filename length
# Sample usage:

# fd = os.open( "Today.txt", os.O_RDWR)
# info = os.fstatvfs(fd)
# print(f"File Info: {info}")
# print(f"Maximum filename length: {info.f_namemax}")
# print (f"Free blocks: {info.f_bfree}")
# os.close( fd)



# 18. fsync(fd)
# This Python os Module forces write on the file liknked to the descriptor fd to disk.

# Beginning with a Python file object f, first execute f.flush(), then perform os.fsync(f.fileno()).

# Do this to ensure all internal buffers linked to f are written to the disk.

# Sample usage:

# fd = os.open( "Today.txt", os.O_RDWR)
# os.write(fd, "Testing")
# os.fsync(fd)
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print("Read String is: {str} ")
# os.close( fd )

# Real-World Use Cases
# Databases and Transaction Logs:
# Databases like SQLite or PostgreSQL use fsync to ensure that transaction data is safely written to disk before marking a transaction as committed. This ensures durability in the event of a system crash.
# File System Reliability:
# Applications that handle critical files, such as configuration files or logs, use fsync after writing to ensure the data is saved on disk immediately and not left in a volatile buffer.
# Crash Recovery:
# Any system that needs to recover from crashes or unexpected power failures relies on fsync to confirm data integrity.
# File Synchronization:
# Tools like file synchronizers or backup utilities use fsync to guarantee that copied or modified files are fully written to the target storage.


# 19. ftruncate(fd,length)
# ftruncate() truncates the file linked to the descriptor fd, so it holds at most length bytes in size.

# Sample usage:

# fd = os.open( "Today.txt", os.O_RDWR)
# os.write(fd, "Testing")
# os.ftruncate(fd, 10)
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print("Read String is: {str}”)
# os.close( fd )

# Real-World Use Cases
# Log Rotation:
# Log management systems truncate large log files to reduce their size while keeping recent entries. This is especially useful for systems with limited disk space.
# Sparse Files:
# In scenarios like virtual machines or databases, sparse files (files that only consume space for the data they contain) are created using ftruncate to allocate a large file size without actually filling it with data.
# File Size Management:
# File servers or applications that manage user quotas might use ftruncate to enforce size limits or reset files to a specific size.
# Preallocating Space:
# When working with large files that grow over time (e.g., media files or database storage files), ftruncate is used to preallocate the required space.



# 20 & 21 getcwd() getcwdu()
# u returns a unicode object that represents the current working directory.
# os.chdir("/var/www/html" )
# print(f"Current working dir: {os.getcwdu()}")
# fd = os.open( "/tmp", os.O_RDONLY )
# os.fchdir(fd)
# print(f"Current working dir: {os.getcwdu()}”)
# os.close( fd )


# 22. isatty(fd)
# isatty()returns True if the descriptor fd is open, and is connected to a tty(-like) device. Otherwise, it returns False.

# Sample usage:

# fd = os.open( "Today.txt", os.O_RDWR)
# os.write(fd, "Testing")
# ret = os.isatty(fd)
# print(f"Returned value is: {ret}")
# os.close( fd )


# 23 lchflags(path,flags)
# This Python os Module sets path flags to the numeric flags. Unlike chflags(), ut doesn’t follow symbolic links.
# The flags may be one of the following values, or a bitwise OR combination of:
# UF_NODUMP − Do not dump the file
# UF_IMMUTABLE − The file may not be changed
# UF_APPEND − The file may only be appended to
# UF_NOUNLINK − The file may not be renamed or deleted
# UF_OPAQUE − The directory is opaque when viewed through a union stack
# SF_ARCHIVED − The file may be archived
# SF_IMMUTABLE − The file may not be changed
# SF_APPEND − The file may only be appended to
# SF_NOUNLINK − The file may not be renamed or deleted
# SF_SNAPSHOT − The file is a snapshot file.

# Key Difference
# chflags affects the target file that the symbolic link points to.
# lchflags affects the symbolic link itself.
# import os
# import stat
# # Example flags (platform-specific, may vary):
# flags = stat.UF_IMMUTABLE  # Example: make the file immutable (not deletable or modifiable)
# # File path (can be a symlink or regular file)
# file_path = "example_file"
# symlink_path = "example_symlink"
# # Setting flags on the target file (via the symlink)
# os.chflags(symlink_path, flags)
# # Setting flags on the symlink itself
# os.lchflags(symlink_path, flags)
# Used in the real
# File System Security
# - Immutable Files: Prevent modification, deletion, or renaming of critical files (e.g., system configs or binaries).
# - Append-Only Files: Ensure logs or other sensitive files are only appended to, not overwritten.
# Backup and Archiving

# Protect files from changes during backups by making them immutable or append-only.
# Preserve archive integrity by locking files against accidental edits.
# Symbolic Link Management

# Use os.lchflags to apply flags specifically to symlinks without altering their target.
# Maintain symlink properties for specialized file systems or deployment tools.
# System Administration

# Automate flag configuration for file system maintenance.
# Mark temporary or sensitive files to restrict their modification or deletion.
# Forensics and Incident Response

# Lock files or logs as immutable to preserve evidence during investigations.
# Ensure files remain unchanged in compromised systems.



# 24. lchmod(path,mode)
# lchmod() 
# Changes the permissions of a symbolic link itself, not the file or directory it points to.
# If the path is a symlink, it affects the symlink, not the target.
# The mode may be one of the following values, or a bitwise OR combination of:

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
# >>> path = "/var/www/html/Today.txt"
# >>> fd = os.open( path, os.O_RDWR )
# >>> os.close( fd )
# >>> os.lchmod( path, stat.S_IXGRP)
# >>> os.lchmod("/tmp/Today.txt", stat.S_IWOTH)
# import os
# import stat
# symlink_path = "example_symlink"
# Set symlink to read-only mode for everyone
# os.lchmod(symlink_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
# import os
# symlink_path = "example_symlink"
# Change ownership of the symlink (not its target) to user ID 1001 and group ID 1001
# os.lchown(symlink_path, 1001, 1001)

# Aspect	lchmod (Change Mode)	lchown (Change Ownership)
# Purpose	Adjusts permissions (who can do what)	Changes ownership (who is responsible)
# Analogy Action	Setting rules for interacting with the signpost	Assigning responsibility for the signpost
# Example Use	Making the signpost read-only to prevent tampering	Transferring the signpost’s upkeep to another team



# 25 lchown(path, uid, gid)
# Changes the owner (user ID) and group (group ID) of a symbolic link, not the file or directory it points to. 
# >>> path = "/var/www/html/Today.txt"
# >>> fd = os.open( path, os.O_RDWR)
# >>> os.close( fd )
# >>> os.lchown( path, 500, -1)
# >>> os.lchown( path, -1, 500)



# 26. link(src,dst)
# Analogy: The Master Key
# Original File (src): Think of this as a master key to a treasure chest.
# Hard Link (dst): This is like creating an exact duplicate of the master key.
# Key Details in the Analogy:
# Same Treasure Chest:
# Both keys (src and dst) open the same treasure chest (the file's data).
# If you add or remove treasure (modify the file's content), the change is visible no matter which key you use.
# Independent Keys:
# If you lose one key (delete src or dst), the other key still works.
# Only when all keys are lost (all hard links are deleted) does the treasure chest disappear (the data is removed from disk).
# No Copying:
# Unlike duplicating the treasure (copying the file), you’re only making a duplicate key. It doesn’t take extra space for the chest itself (the file’s data).
# >>> path = "/var/www/html/Today.txt"
# >>> fd = os.open( path, os.O_RDWR )
# >>> os.close( fd )
# >>> dst = "/tmp/Today.txt"
# >>> os.link( path, dst)


# 27 listdir(path)
# list files and folders in the path last directory
# path = "/Users/oooo/Documents/py/py_path/2024/py/pj"
# dirs = os.listdir( path )
# for file in dirs:
#     print(file)
# print(dir(path))


# 28 lseek(fd,pos,how) 
# pos (Position):
# The offset or position (in bytes) to which the file pointer should move.
# how (Reference Point):
# Specifies how the pos argument is interpreted. It determines the reference point for the new position:
# os.SEEK_SET (0): The offset is relative to the start of the file.
# os.SEEK_CUR (1): The offset is relative to the current position of the file pointer.
# os.SEEK_END (2): The offset is relative to the end of the file.
# fd = os.open( "Today.txt", os.O_RDWR)
# os.write(fd, "This is test")
# os.fsync(fd)
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print(f"Read String is: {str}")
# os.close( fd )

# 30 major(device)
# major() takes a raw device number, and extracts the device major number (usually the st_dev or st_rdev field from stat).
# used to identify if its printer or keyboard etc.
# Sample usage:
# >>> path = "/var/www/html/Today.txt"
# >>> info = os.lstat(path)
# >>> major_dnum = os.major(info.st_dev)
# >>> minor_dnum = os.minor(info.st_dev)
# >>> print(f"Major Device Number: {major_dnum}")
# >>> print(f"Minor Device Number: {minor_dnum}")
# List of Major Device Numbers by Category
# 1. Block Devices (Storage)
# Block devices are devices that store data in fixed-size blocks (e.g., disks).
# Device	Major Number	Description
# SCSI Disk Drives	8	For devices like /dev/sda, /dev/sdb (hard drives).
# IDE Disk Drives	3	Legacy IDE hard drives (/dev/hda, /dev/hdb).
# NVMe Drives	259	Modern NVMe storage devices.
# Loopback Devices	7	Virtual block devices (/dev/loop0, /dev/loop1).
# RAM Disk	1	In-memory block devices (/dev/ram0).
# USB Mass Storage	189	USB drives (external storage).
# 2. Character Devices
# Character devices provide unbuffered, stream-based access (e.g., terminals, printers).
# Device	Major Number	Description
# Serial Ports	4	Legacy serial ports (/dev/ttyS0).
# Pseudo Terminals (PTYs)	5	For virtual terminals (/dev/ptmx).
# Parallel Ports	6	Parallel printers (/dev/lp0).
# Virtual Consoles	7	Text terminals (/dev/tty1).
# Random Number Generator	1	Random data source (/dev/random).
# 3. Input Devices
# Input devices like keyboards and mice.
# Device	Major Number	Description
# Keyboards and Mice	13	Input devices (/dev/input).
# Joysticks	13	Game controllers (/dev/input/js0).
# 4. Network Devices
# Network interfaces provide access to networking hardware.
# Device	Major Number	Description
# Tun/Tap Devices	10	Virtual network interfaces.
# Network Block Device	43	Network-based storage devices.
# 5. Multimedia Devices
# Audio and video input/output devices.
# Device	Major Number	Description
# Audio Devices	14	Sound cards (/dev/dsp).
# Video Capture Devices	81	Webcams and video devices.
# 6. Printers
# Office printers and printing systems.
# Device	Major Number	Description
# Parallel Port Printers	6	Printers attached to parallel ports.
# USB Printers	180	Printers attached via USB.
# How to Check Major and Minor Numbers
# To view the major and minor numbers for devices on your system:
# Using ls -l on /dev:
# ls -l /dev
# Example output:
# brw-rw---- 1 root disk 8, 0 Dec 28 10:00 /dev/sda
# crw-rw---- 1 root root 4, 0 Dec 28 10:00 /dev/ttyS0
# The numbers (8, 0 for /dev/sda) represent the major (8) and minor (0) device numbers.
# Using stat Command:
# stat /dev/sda
# Output:
# Device: 802h/2050d   Inode: 15196    Links: 1
# Device type: 8,0


# 31. makedev(major,minor)
# This Python os Module takes the minor and major device numbers, and creates a raw device number.
# Sample usage:
# >>> path = "/var/www/html/Today.txt"
# >>> info = os.lstat(path)
# >>> major_dnum = os.major(info.st_dev)
# >>> minor_dnum = os.minor(info.st_dev)
# >>> print(f"Major Device Number: {major_dnum}")
# >>> print(f"Minor Device Number: {minor_dnum}")
# >>> dev_num = os.makedev(major_dnum, minor_dnum)
# >>> print(f"Device Number: {dev_num}")

# 1. Creating Device Files
# In Unix-like systems, device files (e.g., /dev/sda, /dev/tty) are used to interact with hardware devices.
# The device ID (generated using os.makedev()) is required when creating or working with these files programmatically.
# Example: System administrators or scripts may use this when creating new device nodes using system tools like mknod.
# 2. Systems Programming
# Low-level tools, drivers, or utilities that manage hardware devices use os.makedev() to encode device IDs for operations such as:
# Comparing devices.
# Creating device nodes dynamically.
# 3. Identifying Devices
# Combine major and minor numbers retrieved from existing device files (using os.major() and os.minor()) to verify or replicate the same device ID elsewhere.
# 4. Backups and Restoration
# Backup utilities may store the major and minor numbers of device files to recreate them later. os.makedev() is used during restoration to generate the correct device ID.
# 5. Testing and Simulation
# When simulating device files in unit tests or virtual environments, os.makedev() can be used to generate mock device IDs.

