from CHAP.pipeline import PipelineItem

class UserProcessor(PipelineItem):
    """Generic user processor.
    """

    def process(self, data):
        """Extract the contents of the input data, add a string to it,
        and return the amended value.

        :param data: input data
        :return: processed data
        """
        # If needed, extract data from a returned value of Reader.read
        #if isinstance(data, list):
        #    if all(isinstance(d, dict) for d in data):
        #        data = data[0]['data']
        #if data is None:
        #    return []

        # user code

        ### Welcome to CHAP notebook, user vkuznet

        # CHAP imports
        from CHAP.pipeline import PipelineItem
        # define pipeline object
        pipeline = PipelineItem()

        # and we return data back to pipeline
        return data
