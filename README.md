# DjangoORM practice

1. Creating (create function):
Create user first_name = u1, last_name = u1.
Create user first_name = u2, last_name = u2.
Create user first_name = u3, last_name = u3.
Create blog title = blog1, author = u1.
Create blog title = blog2, author = u1.
Subscribe users u1,u2 on blog1, u2 on blog2.
Create topic title = topic1, blog = blog1, author = u1.
Create topic title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
Like topic1 by users u1, u2, u3.
2. Editing:

Change first_name of all users to uu1 (edit_all function).
Change first_name to uu1 for users, that have first_name u1 or u2 (edit_u1_u2 function).
3. Deleting:

 Delete users with first_name u1 (delete_u1 function).
 Unsubscribe users with first_name u2 from blogs (unsubscribe_u2_from_blogs function).
4. Find topics that have creating date later than 2018-01-01 (get_topic_created_grated function).

5. Найти топик у которого title заканчивается на content (get_topic_title_ended function).

6. Get two first users (reverse sort by id function) (get_user_with_limit function function).

7. Get quantity of topics in every blog, name field as topic_count, sort by topic_count (get_topic_count function).

8. Get average quantity of the blogs (get_avg_topic_count function).

9. Find blogs that have more than one topic (get_blog_that_have_more_than_one_topic function).

10. Get all topics by author that have first_name u1 (get_topic_by_u1 function).

11. Find users, that don't have blogs, sort by id (get_user_that_dont_have_blog function).

12. Find topic, that was liked by all users (get_topic_that_like_all_users function).

13. Find topics, that have no likes (get_topic_that_dont_have_like function).
