# Automated-Binder-Scanning

### Description

Scan your class binders double-sided quickly without a double-sided scanner! It scan your class binder without scanning each page manually and without re-ordering pages. 

It generates a PDF of your class binder.

### How it works:
It utilizes your scanner's document feeder to scan pages in bulk. After scanning your binder's front and back pages, it merges your scanned front and back pages before generating the PDF.

## Usage
1. Clone this repository and install dependencies by running the command:

	```bash
	git clone git@github.com:EKarton/Automated-Binder-Scanning.git
	cd Automated-Binder-Scanning

	virtualenv -p python3 .
	pip3 install -r requirements.txt
	source bin/activate
	```

2. Partition your class binder into units:

	* Example:
		<div width="100%">
			<p align="center">
		<img src="docs/break.jpg" width="80%"/>
			</p>
		</div>

	* **Note**: the number of pages in each unit must be less than the max. number of pages your scanner can take in via its document feeder

3. For each unit, create a folder with two sub-folders: ```Front pages``` and ```Back pages```


	* Example: from my class binder above, my folder structure would look like:

		```
		CSC 384
		└── Unit 1
			└── Front pages
			└── Back pages
		└── Unit 2
			└── Front pages
			└── Back pages
		└── Unit 3
			└── Front pages
			└── Back pages
		└── Unit 4
			└── Front pages
			└── Back pages
		└── Unit 5
			└── Front pages
			└── Back pages
		└── Unit 6
			└── Front pages
			└── Back pages
		└── Unit 7
			└── Front pages
			└── Back pages
		```

4. Open up your Scanner app

	* Refer to [this guide](docs/open-scanner-app.md) for a detailed explaination on how to open your Scanner app.

5. Start scanning the front pages of the first unit using the document feeder option. 

	* This means in the ```CSC 384/Unit 1/Front pages``` folder, the first page scanned is the front page of your unit's first page.

	* Refer to [this guide](docs/scan-front-pages.md) for a detailed explaination on how to scan the front pages of your unit.

6. Now, start scanning the Back pages of your first unit in **Reversed order** 

	* This means in the ```CSC 384/Unit 1/Back pages``` folder, the first page scanned is the back page of your unit's last page

	* Refer to [this guide](docs/scan-back-pages.md) for a detailed explaination on how to scan the back pages of your unit

7. Go back to step 5 for the rest of your units

	* **NOTE**: Sometimes scanners jam / skip pages. To resolve this, delete the folder with the failed unit and redo scanning the front and Back pages
	

8.  In the terminal, run:
	
	```bash
	python3 src/main.py ${yourpath}
	```

	where ```yourpath``` is the path of your binder folder

	Example:

	```bash
	python3 src/main.py "~/Documents/CSC 384"
	```

### Next Steps:

- [ ] Create a GUI that reduces the amount of manual steps
- [ ] Add test cases


### Usage
Please note that this project is used for educational purposes and is not intended to be used commercially. We are not liable for any damages/changes done by this project.

### Credits
Emilio Kartono, who made the entire project.

### License
This project is protected under the GNU licence. Please refer to the LICENSE.txt for more information.
