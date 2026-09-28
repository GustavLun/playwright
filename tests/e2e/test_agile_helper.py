import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    #Expect a title " to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))


# user Story:
# Som en användare
# vill jag kunna läsa om sprint retrospective
# så att jag slutar en spring på rätt sätt.

# Manuellt test
# 1. surfa till webbsidan
# 2. Klicka på knappen med texten "sista"
# 3. Klicka på knappen med texten "Sprint retrospective"
#4. Leta upp rubriken med texten "Sprint retrospective" (alternativ: väl ut baserat på CSS-klass - fungerar men rekommenderas inte)
# 5. Kontrollera att rubriken är synlig

def test_read_sprint_retrospectuive(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    button_locator = page.get_by_role("button", )
    button_last = button_locator.get_by_text("Sista")
    button_last.click()

    page.get_by_role("button").get_by_text(re.compile("Sprint retrospective")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint retrospective"))

    expect(heading).to_be_visible()
