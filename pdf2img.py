import fitz
# read pdf file
pdf = fitz.open('CSE01_Output.pdf')
# iterate through pdf pages
for page in range(0, len(pdf)):
        # load pages with index
        pages = pdf.loadPage(page)
        # take image of page
        img= pages.getPixmap()
        # save image
        img.writeImage(f'image{page+1}.png')
        
        
|--------------------------------------------|

OUTPUT:
  
it will generate pdf as png file.
