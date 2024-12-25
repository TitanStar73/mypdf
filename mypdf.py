"""
Simple Matplotlib based pdf builder
1. Create new pdf object with myPDF(filename, size=(4, 6), scale=1) #Size is aspect ratio, scale controls dpi, use atleast 5 for good quality
2. Add pages with pdf.addPage([elements])
3. Elements:
    - myText(text, size=15, x=0.5, y=0.5, ha='center', va='center')
    - myGraph(x, y, label='My Graph')
    - myImage(path)
4. Render the pdf with pdf.render()
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg


class myPDF:
    def __init__ (self, filename, size=(4, 6), scale=1):
        self.pdf = PdfPages(filename)
        self.size = (size[0]/max(size), size[1]/max(size))
        self.scale = scale
        self.header = self.scale
        plt.rcParams.update({'font.size': 0.9 * self.scale})
    
    
    def addPage(self, elements = [], size=None, scale=None):
        if size == None:
            size = self.size
        if scale == None:
            scale = self.scale
        fig, axes = plt.subplots(len(elements), len(elements[0]), figsize=(size[0] * scale, size[1] * scale))

        for i in range(len(elements)):
            for j in range(len(elements[0])):
                acceptable = {myText, myGraph, myImage}
                if type(elements[i][j]) not in acceptable:
                    temp = myText(elements[i][j])
                else:
                    temp = elements[i][j]
                if type(elements[i][j]) == myText:
                    axes[i, j].text(elements[i][j].x, elements[i][j].y, elements[i][j].text, fontsize=elements[i][j].size * scale, ha=elements[i][j].ha, va=elements[i][j].va)
                    axes[i, j].axis('off')
                elif type(elements[i][j]) == myGraph:
                    axes[i, j].plot(elements[i][j].x, elements[i][j].y, label=elements[i][j].label)
                    axes[i, j].legend()
                elif type(elements[i][j]) == myImage:
                    img = mpimg.imread(elements[i][j].path)
                    axes[i, j].imshow(img)
                    axes[i, j].axis('off')

        self.pdf.savefig()
        plt.close()

    def render(self):
        self.pdf.close()

class myText:
    def __init__ (self, text, size=0.9, x = 0.5, y = 0.5, ha='center', va='center'):
        self.text = text
        self.size = size
        self.ha = ha
        self.va = va
        self.x = x
        self.y = y

class myGraph:
    def __init__ (self, x, y, label='My Graph'):
        self.x = x
        self.y = y
        self.label = label

class myImage:
    def __init__ (self, path):
        self.path = path
