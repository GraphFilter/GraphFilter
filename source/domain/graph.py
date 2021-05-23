import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np

pg.setConfigOptions(antialias=True)


class Graph(pg.GraphItem):
    remove_signal = QtCore.pyqtSignal(int, list)
    change_position_signal = QtCore.pyqtSignal(np.ndarray)
    canvas_clicked_signal = QtCore.pyqtSignal(float, float)

    def __init__(self):
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        self.click_under_cursor = False
        self.custom_pen = []

        pg.GraphItem.__init__(self)

        self.scatter.sigClicked.connect(self.clicked)

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds
        if 'pos' in self.data:
            npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(npts)
            self.createPen(len(self.data['pos']))
        self.setTexts(self.text)
        self.updateGraph()

    def createPen(self, size):
        self.custom_pen = []
        for i in range(0, size):
            self.custom_pen.append({"width": 1})

    def setTexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)

    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])

    def mouseDragEvent(self, ev):
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            pos = ev.buttonDownPos()
            pts = self.scatter.pointsAt(pos)
            if len(pts) == 0:
                ev.ignore()
                return
            self.dragPoint = pts[0]
            ind = pts[0].data()[0]
            self.dragOffset = self.data['pos'][ind] - pos
        elif ev.isFinish():
            self.dragPoint = None
            return
        else:
            if self.dragPoint is None:
                ev.ignore()
                return

        ind = self.dragPoint.data()[0]
        self.data['pos'][ind] = ev.pos() + self.dragOffset
        self.change_position_signal.emit(self.data['pos'])
        self.updateGraph()
        ev.accept()

    def clicked(self, pts, ev):
        pass
