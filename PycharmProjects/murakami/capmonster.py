from capmonster_python import RecaptchaV2Task

capmonster = RecaptchaV2Task("3935d903104f8c95655a29b7825f5fd8")
task_id = capmonster.create_task("https://murakamiflowers.kaikaikiki.com/register/new", "6LeoiQ4eAAAAAH6gsk9b7Xh7puuGd0KyfrI-RHQY")
result = capmonster.join_task_result(task_id)
