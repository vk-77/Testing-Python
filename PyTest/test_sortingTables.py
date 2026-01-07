

def test_sort(browserInstance):
    driver = browserInstance
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browserSortedVeggies = []
    # click on column header
    # collect all veggie name =browser sorted veggie list, (B,A,C)
    # sort this browser sorted veggie list = New sorted list.(A,B,C)
    # browserSortedList == NewSortedList

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/table/thead/tr/th[1]/span[1]").click()

    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggieWebElements:
        browserSortedVeggies.append(ele.text)

    originalList = browserSortedVeggies.copy()

    browserSortedVeggies.sort()

    assert browserSortedVeggies == originalList