Browser
对应一个浏览器实例（Chromium、Firefox或WebKit），Playwright脚本以启动浏览器实例开始，以关闭浏览器结束。浏览器实例可以在headless或者 headful模式下启动。一个 Browser 可以包含多个 BrowserContext。

BrowserContext
Playwright为每个测试创建一个浏览器上下文，即BrowserContext，浏览器上下文相当于一个全新的浏览器配置文件，提供了完全的测试隔离，并且零开销。创建一个新的浏览器上下文只需要几毫秒，每个上下文都有自己的Cookie、浏览器存储和浏览历史记录。浏览器上下文允许同时打开多个页面并与之交互，每个页面都有自己单独的状态，一个 BrowserContext 可以包含多个 Page。

Page
页面指的是浏览器上下文中的单个选项卡或弹出窗口。在Page中主要完成与页面元素交互，一个 Page 可以包含多个 Frame

Frame
每个页面有一个主框架（page.MainFrame()）,也可以有多个子框架，由 iframe 标签创建产生。在playwright中，无需切换iframe，可以直接定位元素（这点要比selenium方便很多）。