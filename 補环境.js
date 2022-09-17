window = global;
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;
location = {
    'protocol':'https:',
    'hostname':'这里放网耻'
}
navigator = {
    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
 
// 由于篇幅太长就不放完整的代码了 
// 这里放网页上拿来下的那一整块代码就行