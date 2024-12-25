import mypdf

pdf = mypdf.myPDF("output.pdf", size=(4,6), scale=50)
pdf.addPage(
    elements=[
        [mypdf.myText("Hello World1"), mypdf.myGraph([1, 2, 3], [4, 5, 6])],
        [mypdf.myText("Hello World2"), mypdf.myGraph([i for i in range(100)], [i**2 for i in range(100)])],
        [mypdf.myImage("image.png"), mypdf.myText("Hello World3")]
    ]
)
pdf.render()
