#!/usr/bin/env python3
"""
Demo script to showcase the Scientific Calculator interface
"""
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.figure import Figure

def create_interface_mockup():
    """Create a visual mockup of the calculator interface"""
    
    fig = plt.figure(figsize=(12, 14))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Background
    background = Rectangle((0, 0), 10, 14, facecolor='#2c3e50', edgecolor='none')
    ax.add_patch(background)
    
    # Title
    ax.text(5, 13.2, 'Calculadora Científica Completa - Avançada', 
            ha='center', va='center', fontsize=16, fontweight='bold',
            color='white', bbox=dict(boxstyle='round,pad=0.5', facecolor='#34495e'))
    
    # Display
    display = Rectangle((0.5, 11.5), 9, 1.2, facecolor='#ecf0f1', 
                        edgecolor='#2c3e50', linewidth=3)
    ax.add_patch(display)
    ax.text(9.3, 12.1, '2*sin(pi/6)', ha='right', va='center', 
            fontsize=18, color='#2c3e50', fontweight='bold', family='monospace')
    
    # Mode label
    ax.text(5, 11, 'Modo: Calculadora', ha='center', va='center',
            fontsize=10, color='#ecf0f1')
    
    # Button colors
    colors = {
        'danger': '#e74c3c',
        'warning': '#f39c12',
        'secondary': '#95a5a6',
        'success': '#27ae60',
        'info': '#16a085',
        'primary': '#3498db',
        'operator': '#34495e'
    }
    
    # Button layout - Row 1
    buttons_row1 = [
        ('C', 'danger'), ('⌫', 'warning'), ('(', 'secondary'), 
        (')', 'secondary'), ('√', 'info')
    ]
    
    # Button layout - Row 2
    buttons_row2 = [
        ('sin', 'info'), ('cos', 'info'), ('tan', 'info'),
        ('π', 'success'), ('e', 'success')
    ]
    
    # Button layout - Rows 3-6 (numbers and operators)
    buttons_rows = [
        [('7', 'primary'), ('8', 'primary'), ('9', 'primary'), 
         ('÷', 'operator'), ('^', 'operator')],
        [('4', 'primary'), ('5', 'primary'), ('6', 'primary'), 
         ('×', 'operator'), ('!', 'info')],
        [('1', 'primary'), ('2', 'primary'), ('3', 'primary'), 
         ('-', 'operator'), ('log', 'info')],
        [('0', 'primary'), ('.', 'primary'), ('=', 'success'), 
         ('+', 'operator'), ('exp', 'info')]
    ]
    
    all_buttons = [buttons_row1, buttons_row2] + buttons_rows
    
    # Draw buttons
    y_start = 10
    button_width = 1.7
    button_height = 1.2
    x_margin = 0.5
    y_margin = 0.3
    
    for row_idx, row in enumerate(all_buttons):
        y_pos = y_start - (row_idx * (button_height + y_margin))
        for col_idx, (text, color) in enumerate(row):
            x_pos = x_margin + (col_idx * (button_width + 0.2))
            
            # Draw button
            btn = Rectangle((x_pos, y_pos), button_width, button_height,
                          facecolor=colors[color], edgecolor='none',
                          linewidth=0)
            ax.add_patch(btn)
            
            # Button text
            ax.text(x_pos + button_width/2, y_pos + button_height/2, text,
                   ha='center', va='center', fontsize=14, fontweight='bold',
                   color='white')
    
    # Graph buttons at bottom
    graph_buttons = [
        ('📊 Gráfico 2D', '#8e44ad'),
        ('📈 Gráfico 3D', '#e67e22'),
        ('📜 Histórico', '#16a085')
    ]
    
    y_bottom = 1.5
    btn_width = 2.8
    for idx, (text, color) in enumerate(graph_buttons):
        x_pos = 0.5 + (idx * (btn_width + 0.3))
        btn = Rectangle((x_pos, y_bottom), btn_width, 0.8,
                       facecolor=color, edgecolor='none')
        ax.add_patch(btn)
        ax.text(x_pos + btn_width/2, y_bottom + 0.4, text,
               ha='center', va='center', fontsize=11, fontweight='bold',
               color='white')
    
    # Add some decorative elements
    ax.text(5, 0.5, '🎓 Powered by Python, NumPy & Matplotlib', 
            ha='center', va='center', fontsize=9, color='#ecf0f1', style='italic')
    
    plt.tight_layout()
    plt.savefig('/tmp/calculator_interface.png', dpi=150, bbox_inches='tight',
                facecolor='#2c3e50')
    plt.close()
    print("✓ Interface mockup created: /tmp/calculator_interface.png")

def create_sample_graphs():
    """Create sample graphs to showcase capabilities"""
    
    # 2D Function plots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Exemplos de Gráficos da Calculadora Científica', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Trigonometric function
    x1 = np.linspace(-2*np.pi, 2*np.pi, 1000)
    axes[0, 0].plot(x1, np.sin(x1), 'b-', linewidth=2, label='sin(x)')
    axes[0, 0].plot(x1, np.cos(x1), 'r-', linewidth=2, label='cos(x)')
    axes[0, 0].set_title('Funções Trigonométricas', fontweight='bold')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('y')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 2: Exponential and logarithmic
    x2 = np.linspace(0.1, 5, 1000)
    axes[0, 1].plot(x2, np.exp(x2), 'g-', linewidth=2, label='e^x')
    axes[0, 1].plot(x2, np.log(x2), 'm-', linewidth=2, label='ln(x)')
    axes[0, 1].set_title('Funções Exponencial e Logarítmica', fontweight='bold')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('y')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 3: Polynomial functions
    x3 = np.linspace(-3, 3, 1000)
    axes[1, 0].plot(x3, x3**2, 'orange', linewidth=2, label='x²')
    axes[1, 0].plot(x3, x3**3, 'purple', linewidth=2, label='x³')
    axes[1, 0].set_title('Funções Polinomiais', fontweight='bold')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('y')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 4: Damped oscillation
    x4 = np.linspace(0, 10, 1000)
    axes[1, 1].plot(x4, np.sin(x4) * np.exp(-x4/10), 'cyan', linewidth=2)
    axes[1, 1].set_title('Oscilação Amortecida: sin(x)·e^(-x/10)', fontweight='bold')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('y')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig('/tmp/sample_graphs_2d.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ 2D sample graphs created: /tmp/sample_graphs_2d.png")
    
    # 3D Surface plot
    fig = plt.figure(figsize=(12, 10))
    
    # 3D Plot 1: Paraboloid
    ax1 = fig.add_subplot(221, projection='3d')
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z1 = X**2 + Y**2
    surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
    ax1.set_title('Paraboloide: z = x² + y²', fontweight='bold')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # 3D Plot 2: Saddle
    ax2 = fig.add_subplot(222, projection='3d')
    Z2 = X**2 - Y**2
    surf2 = ax2.plot_surface(X, Y, Z2, cmap='coolwarm', alpha=0.8)
    ax2.set_title('Sela: z = x² - y²', fontweight='bold')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    
    # 3D Plot 3: Wave
    ax3 = fig.add_subplot(223, projection='3d')
    Z3 = np.sin(np.sqrt(X**2 + Y**2))
    surf3 = ax3.plot_surface(X, Y, Z3, cmap='plasma', alpha=0.8)
    ax3.set_title('Onda: z = sin(√(x² + y²))', fontweight='bold')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    
    # 3D Plot 4: Ripple
    ax4 = fig.add_subplot(224, projection='3d')
    Z4 = np.sin(X) * np.cos(Y)
    surf4 = ax4.plot_surface(X, Y, Z4, cmap='jet', alpha=0.8)
    ax4.set_title('Ondulação: z = sin(x)·cos(y)', fontweight='bold')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    
    fig.suptitle('Exemplos de Gráficos 3D', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/tmp/sample_graphs_3d.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ 3D sample graphs created: /tmp/sample_graphs_3d.png")

if __name__ == "__main__":
    print("Creating demo visualizations...")
    print()
    create_interface_mockup()
    create_sample_graphs()
    print()
    print("All demo files created successfully!")
    print("Files saved in /tmp/:")
    print("  - calculator_interface.png")
    print("  - sample_graphs_2d.png")
    print("  - sample_graphs_3d.png")
