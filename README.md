# Jobs scraper

## Description

A web scraper to automatically find the amount of job offers of all the specified jobs at once and save the data in a CSV file. Useful to know the demand of a variety of jobs.

## Example

Here is an example output:

```
Enter the location (default: "United States"): Argentina
Enter the job titles (comma-separated) (default: "Frontend Developer,Backend Developer,Game Developer"):
Loading driver, please wait...
In Argentina, December 2023 there are...
- 112 job offers for "Frontend Developer"
- 177 job offers for "Backend Developer"
- 36 job offers for "Game Developer"
Data saved at "D:/Proyectos de Nico/Web/jobs_scraper/Jobs offers in Argentina, 28-12-2023Y 15-42.csv"
Quitting...
```

And this is the saved CSV file:

| Job Title          | Offers Amount |
| ------------------ | ------------- |
| Frontend Developer | 112           |
| Backend Developer  | 177           |
| Game Developer     | 36            |

## Important usage note

If the values seem wrong, try the following things:

- Check if the locations is typed correctly, or try with another one (because if the location doesn't exist, it will search in the US)
- Be more specific with the job titles (because some of them may be misunderstood with other jobs, as the search engine also searches in the jobs' description)

## Installation

First, make sure you have Firefox and its driver installed (more details [here](https://pypi.org/project/selenium/#drivers)). After that,

1. Copy the respository: `git clone https://github.com/nicopujia/jobs_scraper.git`

2. With Python 3.12 installed, create a new enviroment: `python -m venv env`

3. Activate the enviroment. Windows: `env\Scripts\activate`. Linux/Mac: `./env/bin/activate`

4. Install the requirements: `pip install -r requirements.txt`

5. Run it: `python main.py`
