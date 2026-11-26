# Password Creation: 3 Ways To Make It Easier
- Source: https://www.nngroup.com/articles/password-creation/
- Author: Katie Sherwin
- Retrieved: 2026-11-25 with Firecrawl
- Page date: April 26, 2015
- Complete: yes
---
[Saved text: the cookie-consent text, the membership banner, image links (image captions kept) and the closing "Related Courses / Learn More / Related Articles" lists were left out. Article body and references are complete.]

Summary: By making password requirements visible upfront, allowing users to unmask the password, and showing a strength meter, designers can improve the frustrating user experience of creating a password.

For most people, the experience of creating a password is almost exactly the same as it was 20 years ago. Consider for a moment just how _exceptional_ that is, given how much technology has changed in that time. Picture a cell phone from 1995; remember its weight, antenna and tiny dark display. Now picture current smartphones, with large touchscreens, HD cameras, and cloud connectivity for infinite storage. It’s quite a different experience. And yet, [coming up with and remembering compliant passwords is as difficult as it was in 1995](http://www.nngroup.com/articles/human-factors-password-security/). (Password managers, which generate random strings of characters and store them on the users’ behalf, and biometric identifiers such as TouchID are standout exceptions to an otherwise stagnant arena of user-authentication technology.)

We’ve all experienced the following three friction scenarios. By anticipating these frustrations and building our forms with them in mind, we can **prevent the friction** before it happens.

## Show the Rules

Imagine you’re about to buy a pair of shoes from a site you haven’t shopped on before. At checkout, you have to create a password. You’re presented with a crisp, white, rectangle labeled _Create a password_.

You go with your old standby, _hectorthecat,_ and tab forward, only to be slapped on the wrist with an error: “Password must include at least 1 uppercase character.” You try again:

_Hectorthecat_

Error slap: “Password must include at least 1 number.”

_Hectorthecat1_

Error slap: “Password must include at least 1 special character.”

_Hectorthecat1%!_

Error slap: "No spaces or % or ~ < >;"

_Hectorthecat123!!!_

Error slap: "Password cannot contain incremental or decremental sequence of letters or numbers." (This last message is an actual error message from mint.com.)

\[Give up, close the tab, and buy the shoes somewhere else\].

When a system doesn’t show the requirements beforehand, **users are essentially being asked to play a game where the rulebook is hidden**. That’s neither fun, nor fair.

**The Solution:** State the password requirements, and make sure that the user can see them the entire time that the field is selected. If you can successfully reduce some of the technical restrictions, you’ll have less text to display and fewer rules for the user to process, making password creation faster.

It’s not enough to just have a link to password requirements (most people won’t notice it or won’t bother expanding that link); password requirements should be visible at the time when the user is creating the password. (And in case you were considering putting the password requirements inside the label itself, don’t. [Placeholders in form fields are bad for many reasons.](http://www.nngroup.com/articles/form-design-placeholders/))

_In these examples, password requirements are visible by default. The designs will vary depending on your site’s requirements, but each of these examples successfully conveys the restrictions to the user in advance of their typing: TrueBlue.JetBlue.com (top), pplelectric.com (bottom)._

_These password requirements are revealed when the user activates the password field, either by tabbing, clicking, or tapping: Firefox.com (top left), PayPal.com (top right), Alibaba.com (bottom)._

## Show the Input

With complex requirements, users make up a compliant password on the fly, adding characters and symbols until it’s valid. And at that point, it’s not so much the _user’s password_, as it is a random string that fits _this system._ Making matters worse, that string is hidden from the users as they invent it, because most passwords are masked. If they want to remember what they ended up with, people will have to carry that information in their [short-term memory](http://www.nngroup.com/articles/short-term-memory-and-web-usability/), as they create it, thus increasing their [cognitive load](http://www.nngroup.com/articles/minimize-cognitive-load/).

Another downside to masked inputs is that they cover up typos, which the user may not have detected. This is particularly important given that many users create passwords from their mobile devices and tablets. Not surprisingly, research shows that users have more errors when typing in passwords on smaller devices than on desktop computers (Von Zezschwitz, 2014).

**The Solution:** [Allow users to unmask the password](http://www.nngroup.com/articles/stop-password-masking/). Seeing the password will support memory and will allow users to check their work. On desktop, hide the password by default, and next to it, place a checkbox labeled _Show password_. On mobile devices and tablets, show the password by default and let users toggle the visibility with a _Hide password_ control. You can be more permissive on mobile because it’s easier for users to shield their device from shoulder-surfers. People are also less likely to be creating accounts for their most secure services while on a phone.

_These examples allow users to unmask the password: Lan.com (top), Yahoo.com (bottom)._

## Show the Strength Meters

Detailed password-composition requirements force users to jump through what feels like arbitrary hoops. People comply because the site forces them, but they end up creating easily guessable phrases. Satisfying the requirements does not necessarily result in secure passwords when real humans are making them up just to get past the registration screen.

**The Solution:** Motivate people to create better passwords by showing how secure the password is.

A study by Egelman et al. (2013) found that **strength meters motivated users to create stronger passwords**. Visually representing the strength of the user’s password, and showing that there is room for improvement, changes the motivation. The benefit is getting a secure password, instead of just complying with a system’s arbitrary command. It’s a slight mental shift that has a potentially large impact on security. (Moreover, reaching the full green bar adds a modicum of satisfaction in an otherwise joyless task: a nice example of gamification used for good.) In general, [focusing on the benefits](http://www.nngroup.com/articles/user-centric-language/) is an effective way of [persuading users](http://www.nngroup.com/courses/credibility-and-persuasive-web-design/) to use your products or services, and it’s one of the top recommendations in [writing for the web](http://www.nngroup.com/courses/writing/).

_Strength meters encourage users to create stronger passwords: Lan.com (top), Booking.com (bottom)._

Note that **indicating progress toward compliance** isn’t the same as a strength meter. Apple.com and healthcare.gov show you how many hoops you’ve jumped through and which ones are left. A slight copy change could nudge users into feeling more motivated, less bogged down, as they type.

_These password requirements indicate progress towards meeting all the criteria: AppleID.Apple.com (top), Healthcare.gov (bottom)._

## Conclusion

The three recommendations presented here ease the process of creating a password, and they all fall on the side of user experience and interface design. They can be addressed without major technical investment and overhaul. But additionally, I urge usability advocates within organizations to make a case to **simplify password requirements**. Usability professionals typically receive strict security requirements from a separate department. It’s generally accepted that nothing can be done about them. But that’s not the case. (Note that this [conflict between usability and security](http://www.nngroup.com/articles/security-and-human-factors/) has also been around for decades.)

- For the IT and security teams, point to research that shows that standard guidelines for complex passwords are more vulnerable than other types. For example, a study from researchers at Carnegie Mellon University recently showed that “certain combinations of requirements \[for longer passwords\] were both stronger and more usable than the traditional complex policy” (Shay et al., 2014). And reiterate how users who do create complex passwords, often store them in unsafe places (on post-its, in a drawer, under the keyboard, or in a file on their computer), therefore making them easy to find.
- For the product and sales teams, articulate how [users are easily scared off by login walls](http://www.nngroup.com/articles/login-walls/) and complex demands from the system, which results in lower conversions. When [account creation is mission critical](http://www.nngroup.com/articles/affordable_care_act_usability_issues/), the signup process needs to be as simple as possible.

By making a technical case for simplifying requirements, and a business case for a more satisfying user experience, you will be more likely to enable your users to quickly and easily create secure and compliant passwords.

**References:**

- Egelman, S., Sotirakopoulos, A., Muslukhov, I., Beznosov, K., & Herley. C. (2013). [Does my password go up to eleven? The impact of password meters on password selection.](http://research.microsoft.com/apps/pubs/default.aspx?id=192108) In _Proceedings of the SIGCHI Conference on Human Factors in Computing Systems_ (CHI '13). ACM, New York, NY, USA, 2379-2388.
- Komanduri, S., Shay, R., Kelley, P.G., Mazurek, M.L., Bauer, L., Christin, N., … Egelman, S. (2011). [Of passwords and people: Measuring the effect of password-composition policies.](http://users.ece.cmu.edu/~mmazurek/papers/chi2011_passwords_people.pdf) In _Proceedings of the SIGCHI Conference on Human Factors in Computing Systems_ (CHI '11). ACM, New York, NY, USA, 2595-2604. (Warning: link leads to a **PDF file**.)
- Shay, R., Komanduri, S., Durity, A.L., (Seyoung) Huh, P., Mazurek, M.L., Segreti, S.M., … Cranor, L.F. (2014). [Can long passwords be secure and usable?](http://www.umiacs.umd.edu/~mmazurek/papers/chi2014-longpasswords.pdf). In _Proceedings of the 32nd Annual ACM Conference on Human Factors in Computing Systems_ (CHI '14). ACM, New York, NY, USA, 2927-2936. (Warning: link leads to a **PDF file**.)
- Von Zezschwitz, E., De Luca, A., & Hussmann, H. (2014). [Honey, I shrunk the keys: Influences of mobile devices on password composition and authentication performance.](http://www.medien.ifi.lmu.de/pubdb/publications/pub/zezschwitz2014nordichi/zezschwitz2014nordichi.pdf) In _Proceedings of the 8th Nordic Conference on Human-Computer Interaction: Fun, Fast, Foundational_ (NordiCHI '14). ACM, New York, NY, USA, 461-470. (Warning: link leads to a **PDF file**.)
