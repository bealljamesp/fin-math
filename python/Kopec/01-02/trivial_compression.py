class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self._bit_string: int = 1
        for nucleotide in gene.upper():
            self._bit_string <<= 2
            if nucleotide == "A":
                self._bit_string |= 0b00
            elif nucleotide == "C":
                self._bit_string |= 0b01
            elif nucleotide == "G":
                self._bit_string |= 0b10
            elif nucleotide == "T":
                self._bit_string |= 0b11
            else:
                raise ValueError(f"Invalid nucleotide: {nucleotide}")

    def _decompress(self) -> str:
        gene: str = ""
        for i in range(0, self._bit_string.bit_length() - 1, 2):
            bits: int = (self._bit_string >> i) & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
        return gene[::-1]

    def __str__(self) -> str:
        return self._decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = (
        "TAGGGATTAACCGTTATATATATATAGGGATTAACCGTTATATATATATAGGGATTAACCGTTATAT"
    )
    print(f"Original is {getsizeof(original)} bytes")
    compressed: CompressedGene = CompressedGene(original)
    print(f"Compressed is {getsizeof(compressed)} bytes")
    decompressed: str = compressed._decompress()
    print(f"Decompressed is {getsizeof(decompressed)} bytes")
    assert original == decompressed, "Original and decompressed genes do not match!"
    print("Compression and decompression are working correctly.")
