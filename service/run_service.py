from service.util import open_ai_client


class RunService:
    def create(self, thread_id, assistant_id):
        client = open_ai_client.default_client
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        print(run)

    def retrieve(self, thread_id, run_id):
        client = open_ai_client.default_client
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        print(run)

    def list_runs(self, thread_id):
        client = open_ai_client.default_client
        runs = client.beta.threads.runs.list(
            thread_id=thread_id
        )
        print(runs)