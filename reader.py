from PyPDF2 import PdfFileReader, PdfFileWriter

def determineMonth(inMonth):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    retMonth = inMonth + "_" + months[int(inMonth)-1]
    return retMonth

def read(filename_add_on, inYear, inMonth):
    boolR = False
    # Where the original file is located
    in_dir = "E:\\BROTHER"
    # Start of the filename
    filename = "BRNB4220010A8A0_000"
    mon = determineMonth(inMonth)
    # The final directory where the rotated PDF will go
    out_dir = r"C:\\Users\\Nicholas\\Ward Packaging\\Procurement - Documents\\Purchasing Documents\\Pickup Reports\\" + inYear + "\\" + mon
    # Adding .pdf onto filename
    filename += filename_add_on + ".pdf"

    # To see if "_prior" will need to be added onto the filename
    print("Is this pickup report from today?")
    resp = input()
    if resp == "yes":
        boolR = True

    # Opens the PDF
    pdf_in = open(in_dir + "\\" + filename, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    # Rotates all the pages in PDF
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(90)
        pdf_writer.addPage(page)
    # Gets date for the rotated PDF for the filename
    filename = input("What is the date of this PDF?")
    filename += ".pdf"
    filename = filename.replace("/","_")
    # Adds "_prior" to filename
    if boolR:
        filename = filename.replace(".","_prior.")
    # Creates final file in destination directory
    pdf_out = open(out_dir + "\\" + filename, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
