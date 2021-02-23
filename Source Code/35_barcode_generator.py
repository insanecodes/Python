# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter


def generate_barcode(num):
    # Now, let's create an object of EAN13 class and
    # pass the number with the ImageWriter() as the writer
    my_code = EAN13(num, writer=ImageWriter())

    # Our barcode is ready. Let's save it.
    my_code.save("bar_code1")


if __name__ == "__main__":
    generate_barcode(input("Enter 12 Digit Number to generate Bar Code : "))
