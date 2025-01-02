# 31 & 32 Aspect	os.mkdir	os.makedirs
# Creates Intermediate Dirs	No (raises FileNotFoundError)	Yes (creates all missing directories)
# Single vs Nested Dirs	Single directory only	Handles both single and nested dirs
# Handles Existing Dir	Raises FileExistsError	Optional (exist_ok=True avoids error)
# Use Case	Simple directory creation	Building complex directory structures


# 33. minor(device) & major(device)
# In Unix-like systems, device files are special files in the /dev directory that represent hardware devices (e.g., disks, terminals, printers). These files are associated with a device ID, which consists of two parts:

# Major Number: Identifies the type of device (e.g., disk, terminal).
# Minor Number: Identifies a specific device instance within that type (e.g., a specific disk partition).
# Use Case: Helps identify the type of device associated with the device ID.
# device: A device ID, typically retrieved using os.stat() or os.lstat() on a device file.
# import os
# # Path to a device file
# device_path = "/dev/sda"
# # Get metadata about the device file
# stat_info = os.stat(device_path)
# # Extract the major and minor device numbers
# major_number = os.major(stat_info.st_rdev)
# print("Major Number:", major_number)
# Example: 8 typically corresponds to SCSI disk devices on Linux.
# - System Administration:
# System tools or scripts can use the major number to group or categorize devices in /dev.
# - Custom Device Drivers: When creating custom device drivers, major numbers are assigned to the driver to define its device type.
# How Device IDs Work
# Device IDs are stored in a special attribute of a file's metadata called st_rdev. You can retrieve it using os.stat() or os.lstat().

# Example of Device ID Decomposition
# import os
# # Path to a device file
# device_path = "/dev/sda"
# # Get metadata about the device file
# stat_info = os.stat(device_path)
# # Extract major and minor numbers
# major_number = os.major(stat_info.st_rdev)
# minor_number = os.minor(stat_info.st_rdev)
# print("Device ID:", stat_info.st_rdev)
# print("Major Number:", major_number)
# print("Minor Number:", minor_number)
# Output (example):
# Device ID: 2048
# Major Number: 8
# Minor Number: 0
# Here:
# Major Number 8: Represents a block storage device (SCSI disk).
# Minor Number 0: Represents the first disk (/dev/sda).

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



# 35. mkfifo(path[, mode])
# where mkdir() default is 0o777(0777) and mkfifo default octal is 0o600(0666).
# It create a FIFO (First In, First Out) special file, also known as a named pipe, at the specified path. Named pipes enable interprocess communication (IPC) by allowing data to be written by one process and read by another, working like a queue.

# >>> path = "/tmp/hourly"
# >>> os.mkfifo( path, 0644 )
# The os.mkfifo(path[, mode]) function in Python is used to create a FIFO (First In, First Out) special file, also known as a named pipe, at the specified path. Named pipes enable interprocess communication (IPC) by allowing data to be written by one process and read by another, working like a queue.
# Real-World Use Cases of os.mkfifo
# Interprocess Communication (IPC):
# Named pipes allow two or more processes to communicate by passing data in a producer-consumer model. For example:
# Producer process writes data to the named pipe.
# Consumer process reads data from the named pipe.
# This is useful when processes need to share data without relying on intermediate files.
# Logging and Monitoring:
# A process can continuously write logs to a named pipe, while another process reads and monitors the logs in real time.
# This avoids the overhead of writing logs to a physical file.
# Stream Processing:
# A producer can stream data (e.g., video, audio, or text) through a named pipe, and a consumer can process it (e.g., encode, analyze, or display) in real time.
# Simulating File Input for Programs:
# A named pipe can be used to simulate a file for programs that expect file input but should instead process dynamically generated data.
# Decoupling of Processes:
# Using a named pipe allows decoupling of two processes so they can work independently, as long as they adhere to the FIFO read/write behavior.

# Key Points:
# Blocking Behavior:
# Reading from a named pipe blocks until data is available.
# Writing to a named pipe blocks until a reader is available.
# This behavior ensures synchronization between producer and consumer processes.
# Permissions:
# The mode parameter controls who can read/write to the pipe.
# Example: 0o600 allows only the owner to read and write.
# System-Specific:
# Named pipes work on Unix-like systems (Linux, macOS). On Windows, consider using the subprocess module or Windows-specific IPC mechanisms for similar functionality.
# Named vs. Anonymous Pipes:
# Named pipes (via os.mkfifo) exist as a file in the filesystem and can be accessed by multiple unrelated processes.
# Anonymous pipes are created on-the-fly and used only between related processes (e.g., parent and child).

# 36 mknod(filename[, mode=0600, device]) as a way to create special files in a computer's storage system. These files are not just 
# regular documents like Word files or images—they are "special" because they serve unique purposes, such as acting as communication
# tools or helpers for the operating system.
# This Python os Module will create a filesystem node named ‘filename’. This can be a file, a device-special file, or a named pipe.
# Imagine This:
# You’re organizing a large event. You need different tools for different tasks:
# A regular notepad for taking notes (this is like a regular file).
# A tube where one person can send messages to another person (this is like a named pipe).
# A control panel for managing devices like lights or speakers (this is like a device file).

# >>> filename = '/tmp/tmpfile'
# >>> mode = 0600|stat.S_IRUSR
# >>> os.mknod(filename, mode)
#  create special files in a computer's storage system. These files are not just regular documents
# like Word files or images—they are "special" because they serve unique purposes, such as 
# acting as communication tools or helpers for the operating system.


# 37. open(file, flags[, mode])
# The flags may take one of these values, or a bitwise-OR combination of these:

# os.O_RDONLY − open for reading only
# os.O_WRONLY − open for writing only
# os.O_RDWR − open for reading and writing
# os.O_NONBLOCK − do not block on open
# os.O_APPEND − append on each write
# os.O_CREAT − create file if it does not exist
# os.O_TRUNC − truncate size to 0
# os.O_EXCL − error if create and file exists
# os.O_SHLOCK − atomically obtain a shared lock
# os.O_EXLOCK − atomically obtain an exclusive lock
# os.O_DIRECT − eliminate or reduce cache effects
# os.O_FSYNC − synchronous writes
# os.O_NOFOLLOW − do not follow symlinks


# 38. os.openpty() in Python is a function used to create a pseudo-terminal, which consists of a pair of 
# file descriptors: one for the master end and one for the slave end of the terminal.
# A pseudo-terminal is a virtual terminal that acts like a physical terminal (e.g., the command line 
# interface), allowing programs to communicate as if they were interacting with a real terminal. This is useful for
# simulating terminal behavior, controlling command-line programs programmatically, and testing terminal-based applications.
# >>> m,s = os.openpty()
# >>> print(m)
# >>> print(s)
# >>> s = os.ttyname(s)
# >>> print(m)
# >>> print(s)
# or 
# master_fd, slave_fd = os.openpty()
# Data written to one end (master or slave) is received by the other end.

# Use Cases:
# Programmatically Controlling a Shell or Command:
# Simulate interaction with a shell (e.g., sending commands and reading responses).
# Testing Terminal Applications:
# Automate tests for programs that rely on terminal I/O.
# Custom Terminal-Based Interfaces:
# Build tools that intercept and manipulate terminal communication.
import os
# # Open a pseudo-terminal
# master_fd, slave_fd = os.openpty()
# # Write to the slave end (simulates user input in a terminal)
# os.write(slave_fd, b'Hello from slave end!\n')
# # Read from the master end (simulate terminal output to Python)
# output = os.read(master_fd, 1024)
# print(f"Master received: {output.decode()}")
# O/P - Master received: Hello from slave end!

# Real-World Example: Controlling a Shell
# This example shows how to run and control a shell (like /bin/bash) using os.openpty():
# import os
# import pty
# import subprocess

# # Open a pseudo-terminal
# master_fd, slave_fd = os.openpty()

# # Start a shell using the slave end of the pty
# proc = subprocess.Popen(['/bin/bash'], stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, close_fds=True)
# # Interact with the shell via the master_fd
# os.write(master_fd, b'echo Hello from the shell!\n')
# output = os.read(master_fd, 1024)
# print(f"Shell output: {output.decode()}")
# # Clean up
# proc.terminate()
# os.close(master_fd)
# os.close(slave_fd)



# os.pathconf() is a function in Python that retrieves system configuration values related to
#  a specific file or directory. It is used to query limits and settings that apply to filesystems, such as the maximum file
#  name length or maximum number of symbolic links that can be followed.
# Sample usage:
# >>> print(f"{os.pathconf_names}" )
# >>> no = os.pathconf('a2.py', 'PC_NAME_MAX')
# >>> print(f"Maximum length of a filename: {no}")
# >>> no = os.pathconf('a2.py', 'PC_FILESIZEBITS')
# >>> print(f"file size in bits: {no}")
# path: The file or directory path to query.
# name: The name of the configuration setting to retrieve. These are constants from the os module (e.g., os.pathconf_names).
# print(os.pathconf_names)
# Common Configuration Names:
# The os.pathconf_names dictionary contains the valid names you can use with os.pathconf. Some commonly used names are:
# Name	Description
# 'PC_NAME_MAX'	Maximum length of a filename in the directory.
# 'PC_PATH_MAX'	Maximum length of a relative path.
# 'PC_PIPE_BUF'	Maximum size of data written atomically to a pipe.
# 'PC_LINK_MAX'	Maximum number of hard links to a file.
# 'PC_NO_TRUNC'	Whether file names longer than NAME_MAX are truncated.
# Example Usage:
# 1. Checking Maximum File Name Length
# import os
# # Query the maximum file name length for the current directory
# max_name_length = os.pathconf('.', 'PC_NAME_MAX')
# print(f"Maximum file name length: {max_name_length}")
# 2. Checking Maximum Path Length
# import os
# # Query the maximum relative path length
# max_path_length = os.pathconf('.', 'PC_PATH_MAX')
# print(f"Maximum relative path length: {max_path_length}")
# 3. Using a File Path
# import os
# # Query configuration for a specific file
# file_path = '/tmp/example_file'
# name_max = os.pathconf(file_path, 'PC_NAME_MAX')
# print(f"Maximum file name length for {file_path}: {name_max}")
# Error Handling:
# If the specified name is invalid or unsupported on the system, os.pathconf() raises an OSError.
# Use Cases:
# Filesystem-Aware Programming:
# Writing programs that adapt to the filesystem's constraints (e.g., ensuring filenames or paths do not exceed the supported length).
# Portable Code:
# Ensuring compatibility across different platforms by querying limits dynamically instead of hardcoding them.
# Resource Management:
# Understanding limits on pipes, links, or other filesystem attributes when working with files or interprocess communication.





# 40.os.pipe() is a function in Python that creates a unidirectional communication channel between processes, 
# often referred to as a pipe. It provides two file descriptors—one for writing and one for reading—allowing 
# data written to one end of the pipe to be read from the other.
# r, w = os.pipe()
# r: File descriptor for the read end of the pipe.
# w: File descriptor for the write end of the pipe.
#  pipe can only transfer data in one direction:

# Data written to the write end (w) can be read from the read end (r).
# Communication is synchronized: the reader waits for data to be written, and the writer waits for space in the pipe buffer if it's full.

# Use Cases:
# Inter-Process Communication (IPC):
# Allow one process to send data to another process (e.g., parent and child processes).
# Connecting Program Components:
# Pass data from one program component to another in a producer-consumer setup.
# Simulating Simple Message Passing:
# Transfer information between different parts of a program or between scripts.
# Real-World Example: Parent chield communication
# import os
# # Create a pipe
# r, w = os.pipe()
# # Fork a new process
# pid = os.fork()
# if pid == 0:  # Child process
#     os.close(w)  # Close the write end in the child
#     message = os.read(r, 1024).decode()
#     print(f"Child received: {message}")
#     os.close(r)
# else:  # Parent process
#     os.close(r)  # Close the read end in the parent
#     os.write(w, b"Hello from parent!")
#     os.close(w)
# When to Use os.pipe:
# Use os.pipe() when you need lightweight, low-level communication between processes or different parts of your program.
# For more complex scenarios, consider using higher-level abstractions like multiprocessing.Pipe or subprocess for easier process management and communication.
