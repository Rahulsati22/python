from pypdf import PdfMerger

mergedFiles = PdfMerger()

fileList = ['pdf1.pdf', 'pdf2.pdf']
for pdf in fileList:
    mergedFiles.append(pdf)

mergedFiles.write("result.pdf")
mergedFiles.close()
