Feature: Factory Acceptance Testing

		 As a user, I want to check if there is a file list of servers 
		 accessed by FTP protocol and HTTP protocol .

         @tag1
		 Scenario: Factory Method Testing for http
		 Given that I visited the domain "'localhost'" with path "''"
		 When I run the program
		 Then the program was able to fetch the following:
		 |servers|
		 |'google.com,facebook.com'|

		 @tag2
		 Scenario: Factory Method Testing for ftp
		 Given that I visited the domain "'ftp.freebsd.org'" and path "'/pub/FreeBSD/'" in ftp
		 When I run the program ftp
		 Then the program was able to fetch the following in ftp:
		 |servers |
		 |CERT    |