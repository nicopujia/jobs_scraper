import csv
import os
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


DEFAULT_LOCATION = 'United States'
DEFAULT_JOB_TITLES = ['Frontend Developer', 'Backend Developer', 'Game Developer']


def get_job_offers_amount(driver: WebDriver, job_title: str, location: str, timeout_seconds: int = 10) -> int:
    driver.get('https://www.glassdoor.com/Job')
    WebDriverWait(driver, timeout_seconds).until(EC.presence_of_element_located((By.ID, 'searchBar-location'))).send_keys(location)
    WebDriverWait(driver, timeout_seconds).until(EC.element_to_be_clickable((By.ID, 'searchBar-jobTitle'))).send_keys(job_title + Keys.ENTER)
    WebDriverWait(driver, timeout_seconds).until(EC.title_contains('in'))
    return int(driver.title.split(maxsplit=1)[0].replace(',', ''))


def main():
    location = input(f'Enter the location (default: "{DEFAULT_LOCATION}"): ').strip().title() or 'United States'
    user_job_titles = input(f'Enter the job titles (comma-separated) (default: "{','.join(DEFAULT_JOB_TITLES)}"): ')
    job_titles = user_job_titles.split(',') if user_job_titles else DEFAULT_JOB_TITLES
    job_titles = [title.strip() for title in job_titles]
    
    print('Loading driver, please wait...')
    
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    
    try:
        now = datetime.now()
        filename = f'Jobs offers in {location}, {now.strftime('%d-%m-%YY %H-%M')}.csv'
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Job Title', 'Offers Amount'])
            print(f'In {location}, {now.strftime('%B')} {now.year} there are...')
            for job_title in job_titles:
                offers_amount = get_job_offers_amount(driver, job_title, location)
                csv_writer.writerow([job_title, offers_amount])
                print(f'- {offers_amount} job offers for "{job_title}"')
        print(f'Data saved at "{os.getcwd().replace('\\', '/')}/{filename}"')
    except NoSuchElementException:
        print('This is not working because the webpage where the data is scraped has changed and the scraper hasn\'t been updated yet.')
    except KeyboardInterrupt:
        print('The proccess has been cancelled.')
    except TimeoutException:
        print('Requests took too long. Please, check your internet connection and try again.')
    except Exception as e:
        print('An unexpected error ocurred:')
        raise
    finally:
        print('Quitting...')
        driver.quit()


if __name__ == '__main__':
    main()
