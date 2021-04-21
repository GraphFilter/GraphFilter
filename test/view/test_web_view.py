import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

pageSource = """
             <html><head>
             <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">                     
             </script></head>
             <body>
             <p><mathjax style="font-size:2.3em">$$u = \int_{-\infty}^{\infty}(awesome) du$$</mathjax></p>
             </body></html>
             """

app = QApplication(sys.argv)
webView = QWebEngineView()
webView.setHtml(pageSource)
webView.show()
sys.exit(app.exec_())

webView.show()
sys.exit(app.exec_())