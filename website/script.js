const headerNav = document.getElementById("options");
const featuresContainer = document.getElementById("features");

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
});
