from pybricks.tools import multitask, run_task, wait, hub_menu
async def m4(robot):
    await multitask(
        robot.right_attachment_reset(),
        robot.move(1000)
    )