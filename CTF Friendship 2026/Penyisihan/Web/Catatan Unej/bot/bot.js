const puppeteer = require('puppeteer');

const TARGET_URL = process.env.TARGET_URL || 'http://web:5000/';
const FLAG = process.env.FLAG || 'null';

const visit = async () => {
    console.log(`[+] Admin visiting ${TARGET_URL}...`);
    let browser;
    try {
        browser = await puppeteer.launch({
            headless: 'new',
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage', 
                '--ignore-certificate-errors'
            ]
        });

        const page = await browser.newPage();

        await page.setCookie({
            name: 'flag',
            value: FLAG,
            domain: 'web', 
            path: '/',
            httpOnly: false,
            secure: false
        });

        await page.goto(TARGET_URL, {
            waitUntil: 'networkidle2',
            timeout: 5000
        });

        await new Promise(r => setTimeout(r, 3000)); 

        console.log("[+] Visit finished.");

    } catch (e) {
        console.error("[-] Error visiting page:", e.message);
    } finally {
        if (browser) await browser.close();
    }
};

setInterval(visit, 30000);
console.log("[*] Bot started. Visiting every 30s.");