from pybricks.tools import multitask

async def m4(robot):
    await multitask(
        robot.left_attachment_reset(),
        robot.parallel_move(1000)
    )