img_link = '"' + input('IMG   [>>>]  ') + '"'
app_link = '"' + input('URL   [>>>]  ') + '"'
title = input('Title [>>>]  ')
desc = input('Desc  [>>>]  ')

template = f"""<div class="app-container">
  <div class="app-items">
    <img src={img_link}>
  </div>
  <div class="app-items">
    <p><a href={app_link}><b>{title}:</b></a> {desc}</p>
  </div>
</div>
"""

print("\n"+template)
