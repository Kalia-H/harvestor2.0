# harvestor2.0
harvestor v2.0 introduces a Tkinter‑based GUI, making the scraper more user‑friendly and interactive.

**Harvestor2.0** is a Python-based web scraping tool with a Tkinter GUI.  
It allows users to enter any website URL, select an HTML element to parse, and view the extracted results in a clean, interactive table.  
This release introduces a graphical interface and customizable parsing options, making the tool more powerful and user-friendly.

---

## ✨ Features
- **Tkinter GUI** for intuitive interaction
- **Customizable parsing**: choose any HTML element (`<p>`, `<h1>`, `<img>`, etc.)
- **URL validation** with automatic correction for missing protocols
- **Data extraction pipeline**:
  1. Create headers
  2. Fetch HTML
  3. Parse HTML with BeautifulSoup
  4. Extract selected elements
- **Results displayed in a table** within the GUI
- **Export option** to save results (CSV export placeholder included)

## Roadmap
- [ ] Implement CSV export functionality
- [ ] Improve error handling and user feedback
- [ ] Package as an executable for easier distribution
      
---
Author
Kalia Hudson
Harvestor2.0 - November 2025
