package main

import (
	"time"

	"github.com/tebeka/selenium"
)

func l_1_2(driver selenium.WebDriver) error {
	if err := driver.Get("https://suninjuly.github.io/text_input_task.html"); err != nil {
		return err
	}
	time.Sleep(1*time.Millisecond)

	textarea, err := driver.FindElement(selenium.ByCSSSelector, ".textarea")
	if err != nil {
		panic(err)
	}
	textarea.SendKeys("get()")
	time.Sleep(1*time.Millisecond)

	submit_button, err := driver.FindElement(selenium.ByCSSSelector, ".submit-submission")
	if err != nil {
		panic(err)
	}
	submit_button.Click()
	time.Sleep(1*time.Millisecond)

	return nil
}