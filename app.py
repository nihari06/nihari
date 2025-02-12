import streamlit as st

def create_recipe_blog_post(recipe_data):
    """
    Formats recipe data into a blog post structure.
    """
    blog_post = f"""
    ## {recipe_data['title']}
    
    {recipe_data['intro']}
    
    ### Why This Recipe Works:
    
    """
    for point in recipe_data['why_works']:
        blog_post += f"* {point}\n"
    
    blog_post += f"""
    
    ### Recipe:
    
    **Yields:** {recipe_data['yields']}
    **Prep time:** {recipe_data['prep_time']} minutes
    **Cook time:** {recipe_data['cook_time']} minutes
    
    #### Ingredients:
    
    """
    for ingredient in recipe_data['ingredients']:
        blog_post += f"* {ingredient}\n"
    
    blog_post += "\n#### Instructions:\n\n"
    for i, instruction in enumerate(recipe_data['instructions']):
        blog_post += f"{i+1}. {instruction}\n"
    
    if recipe_data['tips']:
        blog_post += f"""
        
        #### Tips & Variations:
        
        * {recipe_data['tips']}
        
        """
    
    blog_post += f"""
    {recipe_data['call_to_action']}
    """
    return blog_post

st.title("Recipe Blog Post Generator")

st.subheader("Enter Recipe Details")

recipe_data = {
    "title": st.text_input("Recipe Title"),
    "intro": st.text_area("Introduction"),
    "why_works": st.text_area("Why This Recipe Works (Separate points with commas)").split(","),
    "yields": st.text_input("Servings"),
    "prep_time": st.number_input("Prep Time (minutes)", min_value=1, step=1),
    "cook_time": st.number_input("Cook Time (minutes)", min_value=1, step=1),
    "ingredients": st.text_area("Ingredients (Separate items with commas)").split(","),
    "instructions": st.text_area("Instructions (Separate steps with new lines)").split("\n"),
    "tips": st.text_area("Tips & Variations"),
    "call_to_action": st.text_area("Call to Action")
}

if st.button("Generate Blog Post"):
    blog_post = create_recipe_blog_post(recipe_data)
    st.subheader("Generated Blog Post")
    st.markdown(blog_post)
