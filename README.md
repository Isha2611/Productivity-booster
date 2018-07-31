# Productivity-Booster
In today's internet age, social networking is at the heart of collaboration, building real-life connections and so much more.
But, you need to admit that sometimes, this takes a toll on your most productive hours. Ever spent hours on Facebook when you just opened it to check the notifications and thought it would take only 5 minutes?

Well, as they say: "Excess of everything is bad". But sometimes, your self-determination is not enough to limit yourself from indulging in social networking during your most productive hours. Worry not! Productivity-booster comes to your rescue.

# What is it?
It is a python-based application which runs in background and blocks specific websites(time-consuming) but only during productive hours. It lets you use them openly during your non-productive hours or Fun hours as we call them.

# How does it work?
It basically starts at the reboot and runs silently in the background all the time. Everytime, you enter a URL in your browser, it needs to resolve it to an ip address. The first place to check is the hosts table. If an entry is found there, it automatically re-directs to that IP address. If not, the request is sent to ISP for resolution. It is called DNS resolution. So, The way this app works is by adding a host entry in the host file of your machine system. That host entry basically redirects the url to the loopback ip address. This stops the request being sent to ISP for DNS resolution and in effect blocks the website access.
Now, while out of office hours, it basically removes the added entries and you are able to access the website again.

# Compatibility
It is Mac,Linux and Windows compatible.

# Where to get it?
For now, you can download it from GitHub. I will be making a packaged application pretty soon.
