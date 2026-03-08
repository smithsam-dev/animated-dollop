import turtle

def draw_grid(t, width, height, step):
    """Draws a faint background grid similar to the reference image."""
    t.color("#EAF2F5") # Faint cyan/blue
    t.pensize(1)
    # Vertical lines
    for x in range(-width//2, width//2, step):
        t.penup()
        t.goto(x, height//2)
        t.pendown()
        t.goto(x, -height//2)
    # Horizontal lines
    for y in range(-height//2, height//2, step):
        t.penup()
        t.goto(width//2, y)
        t.pendown()
        t.goto(-width//2, y)

def draw_polygon(t, points, color, width):
    """Traces a closed polygon given a list of coordinates."""
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(color)
    t.pensize(width)
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0]) # Close the shape

def main():
    # --- Screen Setup ---
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Coding Club Logo")
    screen.bgcolor("#F4F9F9") 
    
    # Disable auto-updates for instant drawing
    screen.tracer(0) 

    t = turtle.Turtle()
    t.hideturtle()
    
    # Draw background grid
    draw_grid(t, 800, 800, 30)

    # --- Logo Styling ---
    logo_color = "#001A99" # Deep navy blue
    pen_weight = 4

    # --- Geometric Coordinates (Mathematically Aligned & Scaled) ---
    
    # Right bracket / Right side of the graduation cap
    right_bracket = [
        (15, 120),    # Top inner
        (105, 75),    # Top outer
        (105, 15),    # Bottom outer
        (15, -30),    # Bottom inner
        (15, 22.5),   # Inner corner up
        (60, 45),     # Point of the '>'
        (15, 67.5)    # Inner corner down
    ]

    # Left bracket / Left side of the graduation cap (Mirrored)
    left_bracket = [
        (-15, 120),   # Top inner
        (-105, 75),   # Top outer
        (-105, 15),   # Bottom outer
        (-15, -30),   # Bottom inner
        (-15, 22.5),  # Inner corner up
        (-60, 45),    # Point of the '<'
        (-15, 67.5)   # Inner corner down
    ]

    # Bottom 'U' Shape / Shield base
    u_shape = [
        (-75, -22.5),   # Left outer top
        (-75, -97.5),   # Left outer bottom
        (0, -135),      # Center outer point
        (75, -97.5),    # Right outer bottom
        (75, -22.5),    # Right outer top
        (52.5, -33.75), # Right inner top
        (52.5, -86.25), # Right inner bottom
        (0, -112.5),    # Center inner point
        (-52.5, -86.25),# Left inner bottom
        (-52.5, -33.75) # Left inner top
    ]

    # --- Draw Main Shapes ---
    draw_polygon(t, right_bracket, logo_color, pen_weight)
    draw_polygon(t, left_bracket, logo_color, pen_weight)
    draw_polygon(t, u_shape, logo_color, pen_weight)

    # --- Draw the Tassel ---
    t.color(logo_color)
    t.pensize(pen_weight)
    
    # Tassel string
    t.penup()
    t.goto(-105, 15)  # Drop from the left edge
    t.pendown()
    t.goto(-105, -15) 

    # Tassel bead
    t.penup()
    t.goto(-105, -24) # Position at the bottom of the circle
    t.setheading(0)
    t.pendown()
    t.circle(4.5)     # Draw circle

    # Tassel fringe (Triangle)
    t.penup()
    t.goto(-105, -24)
    t.pendown()
    t.goto(-115, -50)
    t.goto(-95, -50)
    t.goto(-105, -24)

    # --- Typography ---
    t.penup()
    t.goto(0, -210) # Position below the shield
    t.pendown()
    # Using a clean sans-serif font to match the image
    t.write("CODING CLUB", align="center", font=("Arial", 46, "normal"))

    # Force screen update to show the final drawing
    screen.update()
    turtle.done()

if __name__ == "__main__":
    main()
