# Postmortem: Service Outage Due to 500 Server Errors

[Diagrammatic Link](https://miro.com/app/board/uXjVNoFBTmg=/)

__Incident Date__: August 16, 2024

__Duration__: 2 hours (from 08:00 AM to 10:00 AM WAT)

__Impact__: 100% of users experienced service interruptions, leading to failed requests and an inability to access key functionalities.

__Summary__
On August 16, 2024, our web services experienced a significant downtime characterized by a surge in 500 server errors. These errors, particularly 500 Internal Server Error disrupted service for about two hours, impacting a large portion of our user base. This postmortem provides an in-depth analysis of the incident, outlines the root causes, and discusses the actions taken to restore normal operations and prevent future occurrences.

__Incident Timeline__:
08:00 AM: The first signs of the incident were detected when our monitoring system flagged a spike in 500 Internal Server Error.

08:10 AM: On-call engineers were alerted and began investigating the issue.

08:20 AM: It was identified that a significant number of requests were also failing with 500 Internal Server Error.

08:30 AM: An emergency incident call was initiated to coordinate efforts across the engineering teams.

09:00 AM: Engineers traced the problem using "strace" and "tmux" (terminal multiplexer) to a typographical error in the /var/www/html/wp-settings.php file and a mispelt "php" file extension on line 137.

09:15 AM: The misspelt "phpp" extension was corrected to "php", and a puppet configuration file was used to automate this process.

09:30 AM: Puppet configuration file was run and service was restored.

10:00 AM: Full service was restored, and monitoring confirmed the resolution of the issue.

__Root Cause Analysis__
Missplet .php extension:
There was a typographical error of in the file /var/www/html/wp-settings.php. In this file, on line 137 the expected ".php" extension was named as ".phpp". This made it impossible for the service content in this file to be accessed as served as response to the client or user.

* __Impact__

__User Experience__:

100% of users experienced failed requests and were unable to access key functionalities on our platform during the incident.
Users reported frustration and potential loss of data due to repeated 500 Internal Server Error responses.

__Business__:
The outage resulted in a temporary loss of revenue and negatively impacted customer trust.
Customer support teams received a higher-than-normal volume of inquiries related to the service disruption.

__Resolution__
__Immediate Fixes__:
    - The ".phpp" misspelt extension was corrected to properly access its file contents and retrieve response to a request. This was done with the use of an automated puppet file that used the "sed" command to perform inline text replacement and fix the desired typographical error
    - Automated Testing was carried out to ensure proper file handling and correct repsonse retrieval
    - File Type Validation was implemented for stricter file type check, preventing issues like incorrect file extensions ("phpp") before they get to production

__Long-term Preventative Measures__:
    - Word Press Configuration File Review: Regular audits of wp-settings.php configurations will be scheduled to ensure they remain optimal.
    - Monitoring and Alerts: Setup real-time monitoring system that alerts the team if there is any change in important WordPress configuration files. This allows for quick identification, investigation and remediation.
    - Backup and Version Control: Implement robost backup and version control strategy for WordPress configuration files. This ensures that changes are easily tracked and can be also reverted.
    - Traning and seminar sessions on usage of diagnostic tools used in identifying and fixing the bug. These includes __strace, tmux, linux search commands, puppet, ruby, puppet-lint__. This will help engineers be better equipped and prevent or fix future tasks.

* __Lessons Learned__

__Importance of Configuration Audits__: Regular configuration reviews are critical to catching potential issues before they lead to outages/downtime. The misconfiguration in the wp-settings.php could have been prevented with a more rigorous audit process.

__Need for File type validation__: File type validation performs file type check, catching bugs in development, before it gets to production.

__Enhanced Monitoring__: The incident highlighted gaps in our monitoring setup, particularly around file type validation. We will be enhancing our monitoring systems to provide more granular insights and quicker alerts.

* __Conclusion__

This incident underscored the need for ongoing vigilance in system configuration and capacity planning. While the  was error resolved within two hours, the impact on our users and business was significant. By implementing the corrective actions outlined above, we are committed to improving the resilience of our systems and preventing similar incidents in the future.

__Action Items__:

 Schedule regular file validation audit checks.
 Enhance server response capacity through planning, automation and monitoring.
 Update monitoring tools for better visibility into system performance under load.
Prepared by: [Egbuniwe Emmanuel]
Date: August 18, 2024
Reviewed by: [Blessing Chidewu]
Version: 1.0
