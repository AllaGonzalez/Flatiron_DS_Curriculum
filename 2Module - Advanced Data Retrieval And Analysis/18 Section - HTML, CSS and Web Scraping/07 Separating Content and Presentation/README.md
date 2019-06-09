
# Seperating Content and Presentation

## Introduction
We now know what HTML is. We know how to create a properly-formatted HTML
document and we know how to browse the HTML references. We have everything
we need to be HTML authors. However, if we look at our rendered HTML pages, we
can't help but notice that they look a little plain. How do we make them look
more attractive?  And why can't we make our pages look better with only HTML
itself? We'll solve those questions in this lesson.

## Objectives
You will be able to:
* Identify the separation of content and presentation
* Identify the role of CSS

## Identify the Separation of Content and Presentation

HTML lets us mark-up our content with semantic _structure_. This is what lets
us build solid foundations for our content and it's the chief purpose of HTML.

It would be great to be able to say, "Browser, when you see a `p` tag with
`id` of `my-name`, make the first letter be huge!" Or, to get your readers'
attention, you might say, "Browser, if you see _any_ tag with a `class` of
`warning` surround it with a red box!"

HTML authors believe that creating marked-up documents and styling marked-up
documents are entirely separate tasks. They see a difference between writing
_content_ (the data within the HTML document) and specifying _presentation_,
the rules for displaying the rendered elements.  We use HTML for content and

## Identify the Role of CSS

CSS, or "Cascading Style Sheets," tell us how to write rules that define how
browsers will present HTML. Rules in CSS won't look like HTML and they usually
live in a file apart from our HTML file.

CSS handles all of the ways we want to customize our content's look and feel
from margins and colors, to column-based layout!

## Additional Resources

* [CSS Guidelines: The Separation of Concerns](https://cssguidelin.es/#the-separation-of-concerns)
* [CSS Zen Garden](http://www.csszengarden.com/)

## Summary
We separate the content of our HTML pages from their presentation, which we
style with CSS. By keeping the two separate, we not only utilize the best tools
for each job, but we can change code for one without disturbing the code for
the other.
