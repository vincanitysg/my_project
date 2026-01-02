from qr.generator import generate_qr

def main():
    text = "https://example.com"
    output = "example.png"
    generate_qr(text, output)
    print(f"QR code saved to {output}")

if __name__ == "__main__":
    main()
