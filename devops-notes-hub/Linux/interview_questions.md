# 🐧 Linux Interview Preparation Guide (DevOps-Focused)

## 🧩 1. Commonly Asked Linux Interview Questions

| No. | Question | Short Answer / Explanation | Example Command / Output |
|-----|-----------|-----------------------------|---------------------------|
| 1 | What is the difference between `apt` and `yum`? | `apt` is used in Debian/Ubuntu, `yum` is used in RHEL/CentOS. Both are package managers. | `sudo apt install nginx` or `sudo yum install nginx` |
| 2 | How do you check disk usage in Linux? | Use `df` for filesystem space and `du` for directory usage. | `df -h` or `du -sh /var/log` |
| 3 | How to find a running process by name? | Use `ps` or `pgrep` to list process details. | `ps aux | grep nginx` or `pgrep nginx` |
| 4 | How do you find which port a process is using? | Use `netstat` or `ss` commands. | `sudo netstat -tulnp` or `sudo ss -tulnp` |
| 5 | What does `chmod 755` mean? | Owner: read/write/execute; Group/Others: read/execute. | `chmod 755 script.sh` |
| 6 | How to view real-time system resource usage? | Use `top` or `htop` for live system metrics. | `top` |
| 7 | What is the difference between `hard` and `soft` links? | Hard links share the same inode; soft links (symlinks) reference the file path. | `ln file1 file2` (hard), `ln -s file1 link1` (soft) |
| 8 | How do you check system uptime? | Shows how long the system has been running. | `uptime` |
| 9 | How to view last 10 lines of a log file continuously? | Use `tail -f` to stream logs. | `tail -f /var/log/syslog` |
| 10 | How to check environment variables? | Use `env` or `printenv`. | `printenv PATH` |

---

## ⚙️ 2. Moderate-Level Linux Interview Questions

| No. | Question | Short Answer / Explanation | Example Command / Output |
|-----|-----------|-----------------------------|---------------------------|
| 1 | How to schedule a job in Linux? | Use `cron` for recurring and `at` for one-time jobs. | `crontab -e` |
| 2 | How do you check and kill a process consuming high CPU? | Find using `top`/`ps`, then kill using PID. | `kill -9 <pid>` |
| 3 | What is the difference between `su` and `sudo`? | `su` switches users; `sudo` runs commands as another user temporarily. | `sudo systemctl restart nginx` |
| 4 | How do you find the top 10 memory-consuming processes? | Use `ps` sorted by memory usage. | `ps aux --sort=-%mem | head -10` |
| 5 | How do you find files modified in the last 24 hours? | Use `find` with `-mtime` option. | `find /var -mtime -1 -type f` |
| 6 | How do you redirect both stdout and stderr to a file? | Combine using `&>` or `2>&1`. | `command &> output.log` |
| 7 | What is the difference between `/etc/passwd` and `/etc/shadow`? | `/etc/passwd` stores user info; `/etc/shadow` stores hashed passwords. | `cat /etc/passwd` |
| 8 | How do you check open ports on a server? | Use `netstat`, `ss`, or `nmap`. | `sudo ss -tuln` |
| 9 | How to view the boot logs? | Use `journalctl` for systemd logs. | `journalctl -b` |
| 10 | How do you check current runlevel? | Shows system boot mode. | `who -r` or `systemctl get-default` |

---

## 🚀 3. Advanced-Level Linux Interview Questions

| No. | Question | Short Answer / Explanation | Example Command / Output |
|-----|-----------|-----------------------------|---------------------------|
| 1 | How do you troubleshoot high load average? | Check CPU, memory, I/O, and zombie processes. | `uptime`, `top`, `iostat` |
| 2 | How do you check I/O performance in Linux? | Use `iostat`, `iotop`, or `sar`. | `iostat -xz 1` |
| 3 | How do you analyze logs efficiently on large servers? | Use `grep`, `awk`, `sed`, and `cut` together. | `grep ERROR /var/log/app.log | awk '{print $5}' | sort | uniq -c` |
| 4 | How to secure SSH access on a production server? | Disable root login, change default port, use key-based auth. | Edit `/etc/ssh/sshd_config` |
| 5 | How do you identify zombie processes? | Zombies have `<defunct>` status in `ps`. | `ps aux | grep defunct` |
| 6 | How do you check which user ran a command recently? | Use `history` and `auditd` logs. | `ausearch -x <command>` |
| 7 | How do you check memory usage by process? | Use `pmap` or `smem`. | `pmap <pid>` |
| 8 | How do you monitor real-time network traffic? | Use `iftop` or `nload`. | `sudo iftop` |
| 9 | How do you perform kernel tuning? | Modify `/etc/sysctl.conf` and apply with `sysctl -p`. | `sysctl -w net.ipv4.ip_forward=1` |
| 10 | How do you check which file uses most space on server? | Combine `du` and `sort`. | `du -ah / | sort -rh | head -10` |

---

## 🧠 4. Scenario-Based Linux Interview Questions

| No. | Scenario | Short Answer / Explanation | Example Solution |
|-----|-----------|-----------------------------|------------------|
| 1 | CPU usage suddenly spikes to 100%. How do you debug? | Use `top`/`htop` to identify process, then analyze with `strace` or `lsof`. | `top → kill <pid>` |
| 2 | A service is not starting even after `systemctl restart`. | Check logs using `journalctl -xe` or service logs in `/var/log/`. | `journalctl -u nginx.service` |
| 3 | You need to automate cleanup of old log files. | Use a cron job with `find` and `rm`. | `find /var/log -type f -mtime +7 -delete` |
| 4 | A port is blocked, but firewall rules seem fine. | Check SELinux and `iptables` policies. | `sestatus`, `iptables -L` |
| 5 | Your disk is full, but `du` doesn’t show large files. | Deleted open files may still occupy space. Check with `lsof`. | `lsof | grep deleted` |
| 6 | Web app is slow; how to debug? | Check CPU, memory, I/O, and network bottlenecks. | `vmstat 1`, `iostat`, `iftop` |
| 7 | SSH login is very slow. | Check DNS resolution and GSSAPI settings. | Disable `GSSAPIAuthentication` in `sshd_config`. |
| 8 | Need to find who deleted a file. | Use `auditd` to monitor file changes. | `auditctl -w /path/to/file -p wa` |
| 9 | Automate deployment logs archiving every day. | Add a cron job to compress and move logs. | `tar -czf logs_$(date +%F).tar.gz /var/log/app/` |
| 10 | After kernel upgrade, system fails to boot. | Boot using previous kernel from GRUB menu and roll back. | Edit GRUB → select old kernel. |

