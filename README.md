//Here's the complete function reference for XPath Automator:

//🧭 Navigation
js:	
await GoToURL("https://example.com")      // navigate current tab
await newTab("https://example.com")       // open new tab, returns tabId
await closeTab()                          // close current tab
await reload()                            // reload current tab
await switchTab(1)                        // switch by index (1-based)
await switchTab(tabId)                    // switch by real tab ID
await getURL()                            // returns current tab URL

//⏱ Timing
js:	
await Wait(2000)                          // wait ms (pause/stop aware)
await waitForElement('//div', 8000)       // wait until element appears (timeout ms)
await randomWait(800, 2000)               // random wait between min/max ms

//🖱 Mouse & Interaction
js:	
await click('//button[@id="submit"]')
await hover('//nav//a[text()="Menu"]')    // full mouseover/mouseenter sequence
await moveMouseTo('//button')             // realistic curved mouse path to element
await selectOption('//select', "value")  // select dropdown option

//⌨️ Typing
js:	
await fill('//input', "text")             // human-like typing, 80ms/char default
await fill('//input', "text", 50)         // fixed delay per keystroke
await fill('//input', "text", [70, 150])  // random delay range per keystroke

//🔍 Reading
js:	
await check('//input[@id="q"]')           // returns true/false
await extractText('//h1')                 // returns trimmed text
await extractAll('//ul//li')              // returns array of text
await getAttribute('//a', "href")         // returns attribute value
await getCoords('//button')               // returns { x, y, top, left, width, height, absX, absY }
await logElement('//input')              // returns { tag, id, classes, text, visible, rect }

//📜 Scrolling
js:	
await scrollTo('//section[@id="contact"]') // smooth scroll element into view
await scrollV(500)                          // scroll down 500px  (negative = up)
await scrollH(200)                          // scroll right 200px (negative = left)

//🔁 Control Flow
js:	
await retry(() => click('//btn'), 3)                    // retry up to N times
await ifExists('//div[@class="popup"]', async () => {   // run only if element found
  await click('//button[@id="close"]')
})

//📁 Data — Reading
js:	
await getFileContent("data.txt")          // full file as string
await getLineFileContent("list.txt", 3)   // specific line number
await getCSVRow("users.csv", 2)           // specific row as object

//💾 Data — Writing
js:	
await exportCSV([                          // array of objects
  { name: "Alice", score: 95 },
], "results.csv")

await exportCSV([                          // array of arrays
  ["name", "score"],
  ["Alice", 95],
], "results.csv")

await exportCSV("name,score\nAlice,95", "results.csv")  // raw string
// → saved to xpa/downloads/results.csv
// → if file exists, rows are appended (header skipped automatically)

//📸 Screenshot
js:	
await screenshot()                        // → screenshots/screenshot-2026-03-06T14-22.png
await screenshot("before-login")          // → screenshots/before-login-2026-03-06T14-22.png

//🗄 Storage (cross-script memory)
js:	
await store("key", "value")               // save a value
await retrieve("key")                     // get a saved value

//🌐 Proxy
js:	
await checkConnectedProxy()               // returns true/false
await changeProxy()                       // random proxy from datasource/proxies.csv
await clearProxy()                        // back to direct connection

//👤 Profile
js:	
await getProfileName()                    // returns set name or "profile-xxxxxxxx"
await setProfileName("work-profile")      // set once per profile

//⏸ Flow Control
js:	
await PauseUntilResumed()                 // pause until Resume clicked in sidebar
highlightSelectedElements = true          // highlight every targeted element in blue
highlightSelectedElements = false         // turn off

//🛠 Utility
js
random(1, 10)                             // random integer between min and max
logprint("message")                       // print to console tab


---

// //🚀 CLI Launch

firefox.exe -P myprofile -no-remote "http://xpa.local/?m=wiki.js"


---

//**Folder structure:**

xpa/
├── scripts/       ← your .js scripts
├── datasource/    ← input files (CSV, TXT, proxies.csv)
├── downloads/     ← exportCSV output
└── screenshots/   ← screenshot output

\Firefox Nightly\defaults\pref

autoconfig.js

Firefox Nightly\distribution

policies.json


Firefox Nightly\

mozilla.cfg
