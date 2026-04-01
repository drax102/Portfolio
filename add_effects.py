import os

# 1. Append CSS to style.css
css_to_add = """

/* --- NEW FANTASTIC EFFECTS --- */

/* Scanning Pulse */
.scanline {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 10px;
    background: linear-gradient(to bottom, transparent, rgba(255, 0, 0, 0.8), transparent);
    animation: scanline 8s linear infinite;
    z-index: 9998;
    pointer-events: none;
    box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
}
@keyframes scanline {
    0% { top: -10%; }
    100% { top: 110%; }
}

/* Glitch Text Effect */
.glitch-text {
    position: relative;
}
.glitch-text::before, .glitch-text::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: transparent;
    pointer-events: none;
}
.glitch-text::before {
    left: 2px;
    text-shadow: -2px 0 var(--accent);
    clip: rect(24px, 550px, 90px, 0);
    animation: glitch-anim-2 3s infinite linear alternate-reverse;
}
.glitch-text::after {
    left: -2px;
    text-shadow: -2px 0 var(--text-primary);
    clip: rect(85px, 550px, 140px, 0);
    animation: glitch-anim 2.5s infinite linear alternate-reverse;
}
@keyframes glitch-anim {
    0% { clip: rect(20px, 9999px, 86px, 0); }
    20% { clip: rect(67px, 9999px, 14px, 0); }
    40% { clip: rect(32px, 9999px, 5px, 0); }
    60% { clip: rect(98px, 9999px, 45px, 0); }
    80% { clip: rect(12px, 9999px, 78px, 0); }
    100% { clip: rect(45px, 9999px, 23px, 0); }
}
@keyframes glitch-anim-2 {
    0% { clip: rect(15px, 9999px, 94px, 0); }
    20% { clip: rect(86px, 9999px, 11px, 0); }
    40% { clip: rect(4px, 9999px, 34px, 0); }
    60% { clip: rect(67px, 9999px, 76px, 0); }
    80% { clip: rect(23px, 9999px, 45px, 0); }
    100% { clip: rect(98px, 9999px, 12px, 0); }
}

/* Cyber-Circuitry Tracing on Hover */
.skill-card::after, .project-item::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    z-index: 10;
    pointer-events: none;
    border-radius: inherit;
}
.skill-card:hover::after, .project-item:hover::after {
    border-color: var(--accent);
    box-shadow: inset 0 0 20px rgba(255, 0, 0, 0.2), 0 0 15px rgba(255, 0, 0, 0.5);
    animation: circuit-trace 2s linear infinite;
}
@keyframes circuit-trace {
    0% { clip-path: polygon(0 0, 100% 0, 100% 10%, 0 10%); }
    25% { clip-path: polygon(90% 0, 100% 0, 100% 100%, 90% 100%); }
    50% { clip-path: polygon(0 90%, 100% 90%, 100% 100%, 0 100%); }
    75% { clip-path: polygon(0 0, 10% 0, 10% 100%, 0 100%); }
    100% { clip-path: polygon(0 0, 100% 0, 100% 10%, 0 10%); }
}

/* Enhanced Glitch hover for primary buttons */
.cta-btn:hover {
    animation: button-glitch 0.3s cubic-bezier(.25, .46, .45, .94) both infinite;
}
@keyframes button-glitch {
    0% { transform: translate(0) }
    20% { transform: translate(-2px, 2px) }
    40% { transform: translate(-2px, -2px) }
    60% { transform: translate(2px, 2px) }
    80% { transform: translate(2px, -2px) }
    100% { transform: translate(0) }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add scanline to body
if '<div class="scanline"></div>' not in html:
    html = html.replace('<body>', '<body>\n\n<!-- Scanning Pulse -->\n<div class="scanline"></div>')

# Add glitch-text to main heading
html = html.replace('<h1 class="main-heading">Utkarsh Srivastava</h1>', '<h1 class="main-heading glitch-text" data-text="Utkarsh Srivastava">Utkarsh Srivastava</h1>')

# Add reactive matrix rain
reactive_matrix_code = """
        // Add hover effect
        column.addEventListener('mouseover', () => {
            column.style.color = '#ffffff';
            column.style.textShadow = '0 0 10px #ffffff';
            column.style.fontWeight = 'bold';
            setTimeout(() => {
                column.style.color = '';
                column.style.textShadow = '';
                column.style.fontWeight = '';
            }, 500);
        });
        
        matrixContainer.appendChild(column);
"""
# Replace the end of createMatrixRain function
html = html.replace('matrixContainer.appendChild(column);', reactive_matrix_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fantastic effects added successfully!")
