const headerNav = document.getElementById("options");
const featuresContainer = document.getElementById("features");
const featuresGrid = document.getElementById("features-grid");

document.addEventListener("DOMContentLoaded", () => {
    if (headerNav) for (const option of headerNav.children) {
        const className = "active";
        option.addEventListener("click", (e) => {
            e.preventDefault();
            if (!option.classList.contains(className)) {
                document.querySelectorAll(`.${className}`).forEach(el =>
                    el.classList.remove(className)
                );
                option.classList.add(className);
            }
        });
    }
    if (featuresContainer) {
        const features = [
            "Core Math", "Number Theory", "Fractions",
            "Polynomials", "Sequences & Finance", "Scientific Tools",
        ];
        for (const feature of features) {
            const li = document.createElement("li");
            li.textContent = feature;
            li.classList.add("box");
            featuresContainer.appendChild(li);
        }
    }
    if (featuresGrid) {
        const features = {
            "Core Math": [
                "Basic Arithmetic (+, -, *, /)", "Expression Evaluation",
                "Calculation History", "Remainder Calculation",
                "Factorial", "Permutations", "Combinations",
            ],
            "Number Theory": [
                "Prime Checker", "Semiprime Checker",
                "Prime Sequence Generator", "Semiprime Sequence Generator",
                "Factorization", "LCM", "GCD",
            ],
            "Fractions": [
                "Fraction to Decimal", "Decimal to Fraction",
                "Proper Fraction Conversion", "Numerator / Denominator",
            ],
            "Polynomials": [
                "Get Coefficients", "Get Terms",
                "Get Variables", "Type by Term",
                "Type by Degree",
            ],
            "Sequence & Finance": [
                "Arithmetic Sequence", "Arithmetic Series",
                "Arithmetic Difference", "Interest Calculations",
            ],
            "Scientific Tools": [
                "Significant Figures (Count & Convert)", "Chemistry Support",
                "Valence & Ion Detection", "Group / Period Finder",
            ],
        }
        for (const group in features) {
            const div = document.createElement("div");
            const h3 = document.createElement("h3");
            const ul = document.createElement("ul");
            div.className = "feature-group";
            h3.textContent = group;
            for (const feature of features[group]) {
                const li = document.createElement("li");
                li.textContent = feature;
                ul.appendChild(li);
            }
            div.appendChild(h3);
            div.appendChild(ul);
            featuresGrid.appendChild(div);
        }
    }
});
