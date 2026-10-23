class AbhishekSharma:
    def highlight(self):
        print("Abhishek Sharma is aggressive left hand batsman")

class VaibhavSuryaVamshi(AbhishekSharma):
    def highlight(self):
        super().highlight()
        print("Vaibhav Surya Vamshi is aggressive left hand batsman and is the future replacement for Abhishek Sharma")

vsv = VaibhavSuryaVamshi()
vsv.highlight()