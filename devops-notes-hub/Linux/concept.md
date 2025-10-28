# 🧠 Linux Topics with Commands — For 5 Years Experienced DevOps Engineer

A complete Linux command + concept reference for DevOps/SRE engineers.

---

## 📌 Table of Contents
- [🟢 1. Linux Basics](#-1-linux-basics)
- [🟡 2. File & Directory Management](#-2-file--directory-management)
- [🔵 3. Text Processing & Filters](#-3-text-processing--filters)
- [🟣 4. Process Management](#-4-process-management)
- [🔴 5. User & Group Management](#-5-user--group-management)
- [🟤 6. File Permissions & Ownership](#-6-file-permissions--ownership)
- [⚪ 7. Disk Management](#-7-disk-management)
- [🟠 8. Network Management](#-8-network-management)
- [🟢 9. Service Management (systemd)](#-9-service-management-systemd)
- [🔵 10. Package Management](#-10-package-management)
- [🟣 11. Logs & Monitoring](#-11-logs--monitoring)
- [🔴 12. System Performance & Troubleshooting](#-12-system-performance--troubleshooting)
- [🟤 13. Crontab & Scheduling](#-13-crontab--scheduling)
- [⚫ 14. Shell Scripting](#-14-shell-scripting)
- [🟣 15. Security & SELinux](#-15-security--selinux)
- [🟢 16. System Info & Hardware](#-16-system-info--hardware)
- [🔵 17. SSH & Remote Access](#-17-ssh--remote-access)
- [🟠 18. System Boot & Startup](#-18-system-boot--startup)
- [🔴 19. Kernel & Modules](#-19-kernel--modules)
- [🟣 20. Interview-Focused Scenarios](#-20-interview-focused-scenarios)

---

## 🟢 1. Linux Basics
<details>
<summary><strong>Concepts & Commands</strong></summary>

### 🧱 Concepts
- Linux Architecture (Kernel, Shell, User space)
- File System Hierarchy: `/etc`, `/var`, `/usr`, `/home`, `/tmp`, `/opt`, `/root`
- Runlevels / systemd targets
- Shell Basics

### 🧰 Commands
```bash
uname -a
hostnamectl
uptime
date
cal
history
whoami
id
pwd
```
</details>

🟡 2. File & Directory Management
<details> <summary><strong>Concepts & Commands</strong></summary>
🧱 Concepts

Navigation, creation, deletion

Hard vs Soft links

Permissions & ownership

🧰 Commands
ls -l
cd /path
mkdir newdir
rmdir olddir
rm -rf folder
cp -r src dest
mv src dest
ln file linkname
ln -s file symlink
chmod 755 file
chown user:group file
find / -name "file.txt"
du -sh *
df -h

</details>

🔵 3. Text Processing & Filters
<details> <summary><strong>Commands & Usage</strong></summary>
🧱 Concepts

Redirection: >, >>, <, |

Pipes & filters

grep, sed, awk mastery

🧰 Commands
cat file.txt
tac file.txt
head -n 10 file.txt
tail -f /var/log/syslog
grep "error" logfile
grep -R "keyword" /etc
awk '{print $1,$3}' file
sed 's/old/new/g' file
cut -d',' -f2 file.csv
sort file.txt | uniq -c
wc -l file.txt

</details>
🟣 4. Process Management
<details> <summary><strong>Commands</strong></summary>
ps aux
top
htop
pgrep nginx
kill -9 1234
nice -n 10 command
renice 5 -p 1234
jobs
bg 1
fg 1

</details>
🔴 5. User & Group Management
<details> <summary><strong>Commands</strong></summary>
useradd devops
passwd devops
usermod -aG docker devops
id devops
groups devops
deluser devops
sudo visudo
su - devops

</details>
🟤 6. File Permissions & Ownership
<details> <summary><strong>Commands</strong></summary>
chmod 644 file
chmod 755 script.sh
chown user:group file
umask 022
getfacl file
setfacl -m u:john:rwx file

</details>
⚪ 7. Disk Management
<details> <summary><strong>Commands</strong></summary>
lsblk
fdisk -l
mount /dev/sdb1 /mnt
umount /mnt
df -h
du -sh /var/*
ls -lh
lsattr file

</details>
🟠 8. Network Management
<details> <summary><strong>Commands</strong></summary>
ip addr show
ping google.com
netstat -tulnp
ss -tulwn
traceroute google.com
nslookup domain.com
dig domain.com
curl -I https://site.com
wget URL
systemctl restart network

</details>
🟢 9. Service Management (systemd)
<details> <summary><strong>Commands</strong></summary>
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl enable nginx
systemctl disable nginx
journalctl -u nginx
systemctl list-units --type=service

</details>
🔵 10. Package Management
<details> <summary><strong>Commands</strong></summary>
Debian/Ubuntu
apt update && apt upgrade
apt install nginx
apt remove nginx
dpkg -l | grep nginx

RHEL/CentOS
yum update
yum install httpd
yum remove httpd
rpm -qa | grep httpd

</details>
🟣 11. Logs & Monitoring
<details><summary><strong>Commands</strong></summary>
tail -f /var/log/messages
less /var/log/syslog
cat /var/log/auth.log
journalctl -xe
dmesg | tail
uptime
vmstat 1
free -m
iostat -xz 1

</details>
🔴 12. System Performance & Troubleshooting
<details><summary><strong>Commands</strong></summary>
top / htop
iotop
vmstat 1
sar -u 1 3
free -h
df -h
dmesg | tail
strace -p PID
lsof -i :80

</details>
🟤 13. Crontab & Scheduling
<details><summary><strong>Commands</strong></summary>
crontab -e
crontab -l
systemctl status cron
at 09:00
atq

</details>
⚫ 14. Shell Scripting
<details><summary><strong>Concept + Example</strong></summary>
#!/bin/bash
for user in $(cat users.txt); do
  echo "Creating $user"
  useradd $user
done

</details>
🟣 15. Security & SELinux
<details><summary><strong>Commands</strong></summary>
getenforce
setenforce 0
sestatus
firewall-cmd --list-all
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --reload

</details>
🟢 16. System Info & Hardware
<details><summary><strong>Commands</strong></summary>
lscpu
lsmem
lsblk
lspci
lsusb
dmidecode | grep -i bios

</details>
🔵 17. SSH & Remote Access
<details><summary><strong>Commands</strong></summary>
ssh user@ip
scp file user@ip:/path
rsync -avz src/ dest/
ssh-keygen
ssh-copy-id user@ip

</details>
🟠 18. System Boot & Startup
<details><summary><strong>Commands</strong></summary>
systemctl get-default
systemctl set-default multi-user.target
grub2-editenv list
dmesg | head
journalctl -b

</details>
🔴 19. Kernel & Modules
<details><summary><strong>Commands</strong></summary>
uname -r
lsmod
modprobe module_name
rmmod module_name

</details>
🟣 20. Interview-Focused Scenarios
<details><summary><strong>Real-World Troubleshooting</strong></summary>

✅ Find top 5 memory-consuming processes

ps aux --sort=-%mem | head -6


🧹 Delete files older than 7 days

find /var/log -type f -mtime +7 -exec rm -f {} \;


🔍 Monitor logs for keyword

tail -f /var/log/syslog | grep --line-buffered "error"


🕵️ Check which process is using a port

lsof -i :8080


💾 Find biggest files

du -ah / | sort -rh | head -20

</details>

