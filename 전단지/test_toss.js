const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({headless: "new"});
  const page = await browser.newPage();
  await page.goto('file:///Users/seunghun/Desktop/데브늄/이음기프트/대학홍보물/전단지/v5_인테이크_토스.html');
  await page.waitForSelector('#step0 .next-btn');
  await page.click('#step0 .next-btn');
  
  await page.waitForSelector('#userName', {visible: true});
  await page.type('#userName', 'Test');
  await page.click('#btn-step1');

  await page.waitForSelector('#userPhone', {visible: true});
  await page.type('#userPhone', '01012345678');
  await page.click('#btn-step2');

  await page.waitForSelector('#univName', {visible: true});
  await page.type('#univName', 'Test Univ');
  await page.click('#btn-step3');

  await page.waitForSelector('#step4 .chip-btn', {visible: true});
  console.log("On Step 4. Waiting 1 second...");
  await page.waitForTimeout(1000);
  
  // click '학생회'
  console.log("Clicking 학생회 chip...");
  const btns = await page.$$('#step4 .chip-btn');
  await btns[2].click();
  
  console.log("Waiting 1 second...");
  await page.waitForTimeout(1000);
  
  // check which step is active
  const activeStep = await page.$eval('.step-section.active', el => el.id);
  console.log("Active step is:", activeStep);
  
  // Click back button
  console.log("Clicking back button...");
  await page.click('.back-btn');
  await page.waitForTimeout(1000);
  
  const backStep = await page.$eval('.step-section.active', el => el.id);
  console.log("Active step after back is:", backStep);

  console.log("Clicking 교직원 chip...");
  await btns[1].click();
  await page.waitForTimeout(1000);
  const finalStep = await page.$eval('.step-section.active', el => el.id);
  console.log("Final active step is:", finalStep);

  await browser.close();
})();
